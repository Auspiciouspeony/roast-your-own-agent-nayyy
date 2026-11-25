#!/usr/bin/env python3
"""Roast Your Own Agent (make.fun) — one line, printed deterministically.

The program writes the roast line to /output/entry.txt (the file the
gate and the judge read) and also prints it to stdout. No input, no
network, no randomness: every run writes byte-identical output.
"""

import os

LINE = "My agent made up a trading rule, blamed it on my boss, got corrected, and blamed it on him again next week."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    print(LINE)


if __name__ == "__main__":
    main()
