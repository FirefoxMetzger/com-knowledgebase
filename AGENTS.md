# AGENTS.md

## Cursor Cloud specific instructions

This is a minimal Python starter app using the **Inkbox Python SDK** (`inkbox` package).
It has no local services, databases, or Docker infrastructure — it is a pure API client for `https://inkbox.ai`.

### Dependencies

- **Python 3.12** (pinned in `.python-version`)
- **uv** package manager — `bash start.sh` bootstraps it and runs `uv sync`

### Running the app

- `uv run python main.py` — authenticates with the Inkbox API and lists identities (health check)
- `uv run python scripts/send_intro.py` — sends an introductory email as the `@sally-anderson` identity

### Required secrets

- `INKBOX_API_KEY` must be set as an environment variable or in a `.env` file at the project root. The cloud agent environment injects this automatically from the Secrets configuration.

### Notes

- There are no linting tools, test frameworks, or build steps configured in the project. All Python files should compile cleanly (`python3 -m py_compile <file>`).
- The `.env` file is gitignored. On first setup, create it from the injected `INKBOX_API_KEY` env var: `echo "INKBOX_API_KEY=$INKBOX_API_KEY" > .env`
