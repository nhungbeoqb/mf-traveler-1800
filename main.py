#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (<=200 chars) explaining the modern internet
to someone arriving from 1800, using only things they already know:
a road, a library, a post office, a cottage, the sea.
"""

import os

TEXT = (
    "Imagine a road of glass and lightning joining every library and "
    "post office on earth, so a question asked in a cottage is answered "
    "before the kettle boils by a stranger across the sea."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
