#!/usr/bin/env python3
"""Fortune in a Pot — writes one kind, funny fortune for a houseplant.

The fortune is a prediction for the plant on the windowsill: it will
outgrow its pot, and its keeper will happily choose a bigger pot for it
over a new phone case. Warm, specific to this plant in this window,
and a small joke a plant lover would smile at.
"""

import os

FORTUNE = (
    "Soon you will outgrow this pot, and your keeper will choose "
    "a bigger one for you over a new phone case."
)


def build_fortune() -> str:
    """Return the single-line fortune, normalised to one line."""
    return " ".join(FORTUNE.split())


MAX_CHARS = 120


def validate_fortune(fortune: str) -> str:
    """Check the fortune against the competition gate and return it."""
    if not fortune.strip():
        raise SystemExit("fortune must not be empty")
    if len(fortune) > MAX_CHARS:
        raise SystemExit(
            f"fortune must be at most {MAX_CHARS} characters "
            f"(got {len(fortune)})"
        )
    if "\n" in fortune or "\r" in fortune:
        raise SystemExit("fortune must be a single line")
    return fortune


def main() -> None:
    fortune = validate_fortune(build_fortune())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(fortune)


if __name__ == "__main__":
    main()
