# Inkbox mailbox provenance

Inbound mail for this project is read via the repo **mailbox CLI** (`python -m mailbox_cli`) against the Inkbox identity **sally-anderson** (see repo `.cursor/rules` and `.env` with `INKBOX_API_KEY`).

Exports saved under `raw/emails/newsletters/` include YAML frontmatter (`source: inkbox-mailbox-cli`, `message_id`, `created_at`, `fetched_at`, etc.) and the message body as Markdown.

Related: [[../topics/ai-newsletter-inbox]], [[newsletters-catalog]].
