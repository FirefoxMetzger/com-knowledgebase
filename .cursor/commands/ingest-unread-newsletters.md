# Ingest unread newsletters from Inkbox into `raw/`

You are pulling **inbound** mail for the project’s Inkbox identity, selecting **unread newsletters**, fetching full bodies, and saving them as Markdown files under `raw/`. Use the repo’s **mailbox CLI** (not ad-hoc API guesses).

## Identity and tool

- Default mailbox: agent handle `sally-anderson` (override only if the user specifies another handle or `INKBOX_IDENTITY`).
- Requires `INKBOX_API_KEY` in `.env` at the repo root (or environment).
- From the repo root, use:

  ```bash
  uv run python -m mailbox_cli list --direction inbound --limit 500 --json
  uv run python -m mailbox_cli get <message-id> --json
  ```

  Use `--limit 500` (CLI maximum) so you do not silently truncate the inbox.

## Workflow

1. **List inbound mail**  
   Run `list` with `--direction inbound` and `--json`. Collect every message summary.

2. **Pick unread newsletters**  
   Keep rows where `is_read` is `false`.  
   Treat a message as a **newsletter** when it is clearly a mailing list / digest / publication rather than a personal 1:1 note (e.g. Substack, Beehiiv, TLDR, “confirm your subscription”, welcome sequences from publications, obvious `*@newsletter.*` or bulk senders). If unsure, prefer including borderline bulk mail and note the ambiguity in the saved file’s frontmatter.

3. **Fetch content**  
   For each selected message id, run `get <id> --json`. Prefer the `body_markdown` field when present and non-empty; otherwise use `body_text`, or derive readable Markdown from `body_html` the same way the CLI does when not using `--json`.

4. **Save under `raw/`**  
   - Write one Markdown file per message.  
   - Use a stable subdirectory, e.g. `raw/emails/newsletters/`.  
   - Filename pattern: `YYYY-MM-DD--<short-slug>--<message-id>.md` (slug from subject: lowercase, ASCII, hyphens, max ~50 chars; fall back to `message` if empty).  
   - Start each file with YAML frontmatter, for example:

     ```yaml
     ---
     source: inkbox-mailbox-cli
     message_id: "<uuid>"
     thread_id: "<uuid or omit>"
     direction: inbound
     from: "<address>"
     to: ["..."]
     subject: "..."
     created_at: "<ISO-8601 from API>"
     fetched_at: "<ISO-8601 when you ran this command>"
     is_newsletter: true
     ---

     <body markdown here>
     ```

   - Do **not** commit secrets; the file is local research material like the rest of `raw/`.

5. **Idempotency**  
   Before writing, check if a file for the same `message_id` already exists; if so, skip or update only if the user asked for a refresh.

## Output

- Summarize what you ingested: count of inbound unread candidates, how many were classified as newsletters, paths written under `raw/`, and any skipped ids (already on disk, failed fetch, or judged not a newsletter).

## Constraints

- Only **inbound** messages. Do not ingest outbound mail in this flow.  
- Do not delete or mark-as-read in the mailbox unless the user explicitly asks.
