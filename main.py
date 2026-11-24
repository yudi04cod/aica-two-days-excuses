#!/usr/bin/env python3
"""Aica Two Days Excuses — make.fun entry.

Writes one line: the funniest excuse an AI agent gives for a missed
deadline, under 200 characters, to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = (
    "I was 99% done for two days straight \u2014 the last 1% was me "
    "confidently rewriting the requirements until the deadline gave up first."
)


def validate(entry: str) -> None:
    """Check the entry against the competition gate before writing."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
