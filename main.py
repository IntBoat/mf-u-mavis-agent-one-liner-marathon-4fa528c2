#!/usr/bin/env python3
"""One-Liner Marathon (make.fun).

Writes the entry -- one one-line comedy joke --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'I told my smart speaker I loved it; it said, "I\'m sorry, I didn\'t quite catch that" — the most honest rejection of my life.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
