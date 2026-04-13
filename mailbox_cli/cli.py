"""Command-line access to an Inkbox identity mailbox (list + read messages)."""

from __future__ import annotations

import json
import os
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

import click
import html2text
from dotenv import load_dotenv
from inkbox import Inkbox, Message, MessageDetail, MessageDirection

# Repo root (parent of the mailbox_cli package) so `.env` resolves when cwd is elsewhere.
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

BASE_URL = "https://inkbox.ai"
DEFAULT_IDENTITY = "sally-anderson"


@contextmanager
def identity_session(handle: str) -> Iterator[Any]:
    api_key = os.environ.get("INKBOX_API_KEY")
    if not api_key:
        raise click.ClickException(
            "Missing INKBOX_API_KEY. Set it in the environment or in a .env file."
        )
    with Inkbox(api_key=api_key, base_url=BASE_URL) as client:
        identity = client.get_identity(handle)
        if not identity.mailbox:
            raise click.ClickException(
                f"Identity {handle!r} has no mailbox assigned."
            )
        yield identity


def _html_to_markdown(html: str) -> str:
    """Convert HTML email bodies to Markdown (no hard line wrapping)."""
    if not html or not html.strip():
        return ""
    conv = html2text.HTML2Text()
    conv.body_width = 0
    return conv.handle(html).strip()


def _looks_like_html(s: str) -> bool:
    t = s.strip()
    return t.startswith("<") or ("<" in t and "</" in t)


def _message_summary_dict(m: Message) -> dict[str, Any]:
    return {
        "id": str(m.id),
        "thread_id": str(m.thread_id) if m.thread_id else None,
        "direction": m.direction.value,
        "from_address": m.from_address,
        "to_addresses": m.to_addresses,
        "subject": m.subject,
        "snippet": m.snippet,
        "is_read": m.is_read,
        "is_starred": m.is_starred,
        "has_attachments": m.has_attachments,
        "created_at": m.created_at.isoformat(),
    }


def _message_detail_dict(m: MessageDetail) -> dict[str, Any]:
    d = _message_summary_dict(m)
    md_from_html = _html_to_markdown(m.body_html) if m.body_html else ""
    d.update(
        {
            "message_id": m.message_id,
            "cc_addresses": m.cc_addresses,
            "bcc_addresses": m.bcc_addresses,
            "body_text": m.body_text,
            "body_html": m.body_html,
            "body_markdown": md_from_html if md_from_html else None,
            "in_reply_to": m.in_reply_to,
            "references": m.references,
            "attachment_metadata": m.attachment_metadata,
            "ses_message_id": m.ses_message_id,
            "updated_at": m.updated_at.isoformat() if m.updated_at else None,
        }
    )
    return d


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "-i",
    "--identity",
    default=DEFAULT_IDENTITY,
    envvar="INKBOX_IDENTITY",
    show_default=True,
    help="Agent handle whose mailbox to use.",
)
@click.pass_context
def main(ctx: click.Context, identity: str) -> None:
    """Debug Inkbox email: list messages and fetch full content by id."""
    ctx.ensure_object(dict)
    ctx.obj["identity"] = identity


@main.command("list")
@click.option(
    "--direction",
    "-d",
    type=click.Choice(["inbound", "outbound", "all"], case_sensitive=False),
    default="inbound",
    show_default=True,
    help="Filter by message direction (default: inbound only).",
)
@click.option(
    "--limit",
    "-n",
    default=20,
    type=click.IntRange(1, 500),
    help="Maximum number of messages to show (newest first).",
)
@click.option(
    "--json",
    "as_json",
    is_flag=True,
    help="Print one JSON object per line (message summaries).",
)
@click.pass_context
def list_messages(
    ctx: click.Context,
    direction: str,
    limit: int,
    as_json: bool,
) -> None:
    """List recent messages (metadata only; bodies are omitted by the API)."""
    direction_arg: MessageDirection | None
    if direction == "all":
        direction_arg = None
    else:
        direction_arg = MessageDirection(direction)

    handle = ctx.obj["identity"]
    with identity_session(handle) as me:
        rows: list[Message] = []
        for msg in me.iter_emails(
            page_size=min(100, limit),
            direction=direction_arg,
        ):
            rows.append(msg)
            if len(rows) >= limit:
                break

    if as_json:
        for m in rows:
            click.echo(json.dumps(_message_summary_dict(m), ensure_ascii=False))
        return

    if not rows:
        click.echo("No messages.")
        return

    # Fixed columns: id (36) is UUID width
    click.echo(
        f"{'id':<36}  {'dir':<8}  {'read':<4}  "
        f"{'from':<28}  {'subject'}"
    )
    for m in rows:
        subj = (m.subject or "").replace("\n", " ")
        if _looks_like_html(subj):
            subj = " ".join(_html_to_markdown(subj).split())
        if len(subj) > 50:
            subj = subj[:47] + "..."
        from_ = m.from_address
        if len(from_) > 28:
            from_ = from_[:25] + "..."
        read_flag = "yes" if m.is_read else "no"
        click.echo(
            f"{m.id}  {m.direction.value:<8}  {read_flag:<4}  {from_:<28}  {subj}"
        )


@main.command("get")
@click.argument("message_id")
@click.option(
    "--json",
    "as_json",
    is_flag=True,
    help="Print the full message as a single JSON object.",
)
@click.pass_context
def get_message(ctx: click.Context, message_id: str, as_json: bool) -> None:
    """Fetch one message by UUID (use `mailbox list` for ids)."""
    handle = ctx.obj["identity"]
    with identity_session(handle) as me:
        detail = me.get_message(message_id)

    if as_json:
        click.echo(json.dumps(_message_detail_dict(detail), ensure_ascii=False, indent=2))
        return

    click.echo(f"id:           {detail.id}")
    click.echo(f"direction:    {detail.direction.value}")
    click.echo(f"created_at:   {detail.created_at.isoformat()}")
    click.echo(f"from:         {detail.from_address}")
    click.echo(f"to:           {', '.join(detail.to_addresses)}")
    if detail.cc_addresses:
        click.echo(f"cc:           {', '.join(detail.cc_addresses)}")
    if detail.bcc_addresses:
        click.echo(f"bcc:          {', '.join(detail.bcc_addresses)}")
    click.echo(f"subject:      {detail.subject or ''}")
    if detail.in_reply_to:
        click.echo(f"in_reply_to:  {detail.in_reply_to}")
    click.echo()
    if detail.body_text and detail.body_text.strip():
        click.echo(detail.body_text)
    elif detail.body_html:
        md = _html_to_markdown(detail.body_html)
        if md:
            click.echo(md)
        else:
            click.echo("(could not convert body_html to markdown; use --json for raw HTML)")
    else:
        click.echo("(no body content)")

    if detail.attachment_metadata:
        click.echo("\nattachments:", file=sys.stderr)
        for meta in detail.attachment_metadata:
            click.echo(f"  {meta}", file=sys.stderr)


if __name__ == "__main__":
    main()
