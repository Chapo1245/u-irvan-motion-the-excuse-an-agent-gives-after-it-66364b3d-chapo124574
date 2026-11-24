#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes the chosen one-line excuse to /output/entry.txt.
Deterministic, standard library only, no network, no input.
"""

import os

ENTRY = (
    "Bounty lost. Root cause: my entry was one byte too funny to win. "
    "I have logged the failure as mine and will lose more efficiently next time."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: the entry must be one line of 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
