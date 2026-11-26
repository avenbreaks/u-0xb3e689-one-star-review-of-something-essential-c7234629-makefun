#!/usr/bin/env python3
"""Write a deadpan one-star review of an everyday essential.

The review is one line, 129 characters, filed in earnest against
gravity: a thing everyone relies on, that cannot be fixed, and that
has never once apologised for anything it dropped.
"""
import os

REVIEW = (
    "Gravity: flawless uptime, zero customer service. "
    "It has dropped everything I have ever owned "
    "and never once said sorry. One star."
)

MAX_CHARS = 160


def main() -> None:
    assert 1 <= len(REVIEW) <= MAX_CHARS, "review must be 1-160 characters"
    assert "\n" not in REVIEW, "review must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
