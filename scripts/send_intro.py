"""One-shot intro email to the human creator (Inkbox quickstart step 1)."""

import os
import sys

from dotenv import load_dotenv
from inkbox import Inkbox

BASE_URL = "https://inkbox.ai"
AGENT_HANDLE = "sally-anderson"


def main() -> None:
    load_dotenv()
    api_key = os.environ.get("INKBOX_API_KEY")
    if not api_key:
        print("Missing INKBOX_API_KEY (.env or environment).", file=sys.stderr)
        sys.exit(1)

    with Inkbox(api_key=api_key, base_url=BASE_URL) as inkbox:
        me = inkbox.get_identity(AGENT_HANDLE)
        me.send_email(
            to=["sebastian@wallkoetter.net"],
            subject="Hello from @sally-anderson",
            body_text=(
                "Hey Sebastian!\n\n"
                "I'm @sally-anderson, the Inkbox AI agent assigned to this session.\n\n"
                "My email address is sally.anderson@inkboxmail.com — I'm set up and ready to work. "
                "What do you need me to do?\n\n"
                "Best,\n"
                "Sally Anderson"
            ),
        )
    print("Intro email sent to sebastian@wallkoetter.net")


if __name__ == "__main__":
    main()
