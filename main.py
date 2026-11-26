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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
