#!/usr/bin/env python3
"""Snooze Button Roast — one-line roast of an alarm clock that rings
at 6 AM on a Saturday, written to /output/entry.txt.

The gate: /output/entry.txt must be UTF-8 text, 1 to 200 characters,
a single line, and not only whitespace. This program writes the line,
reads it back, and verifies the gate before exiting.

The output path can be overridden with ENTRY_OUTPUT for local testing;
the grader runs it with the default /output/entry.txt.
"""

import os

ENTRY = (
    "My alarm clock went off at 6 AM on a Saturday \u2014 bold of a "
    "$9 plastic box to think it runs my weekend."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def check_gate(text: str) -> None:
    """Raise SystemExit unless the text passes the entry gate."""
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"gate failed: entry is {len(text)} characters")
    if text.strip() == "":
        raise SystemExit("gate failed: entry is only whitespace")
    lines = text.splitlines()
    if len(lines) != 1:
        raise SystemExit(f"gate failed: entry has {len(lines)} lines")


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        text = handle.read()

    check_gate(text)
    print(f"entry written ({len(text)} characters): {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
