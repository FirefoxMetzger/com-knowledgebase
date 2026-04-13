"""Minimal Inkbox + uv starter: verify API key and list identities."""

import os
import sys

from dotenv import load_dotenv
from inkbox import Inkbox

INKBOX_BASE_URL = "https://inkbox.ai"


def main() -> None:
    load_dotenv()
    api_key = os.environ.get("INKBOX_API_KEY")
    if not api_key:
        print(
            "Set INKBOX_API_KEY (from https://inkbox.ai/console), then run: uv run python main.py",
            file=sys.stderr,
        )
        sys.exit(1)

    with Inkbox(api_key=api_key, base_url=INKBOX_BASE_URL) as client:
        me = client.whoami()
        print(f"Authenticated as: {me}")

        identities = client.list_identities()
        if not identities:
            print("No identities yet. Create one with client.create_identity(...).")
        else:
            print("Identities:")
            for row in identities:
                print(f"  - {row}")


if __name__ == "__main__":
    main()
