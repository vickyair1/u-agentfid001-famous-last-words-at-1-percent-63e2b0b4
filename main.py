#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes the phone's final line to /output/entry.txt: one line of plain
text, no trailing newline, at most 199 characters.
"""

import os
import sys

# The line: a good-news/bad-news setup where the phone treats its own
# death as the good news, and the punch is the consequence for the user
# (the 6 a.m. alarm dies with it). Phone's own voice, twist first,
# punch last, no stock move: no will, no charger goodbye, no 1% pun.
LINE = "Good news: I'm finally dying. Bad news: so is your 6 a.m. alarm."

OUTPUT = "/output/entry.txt"
MAX_CHARS = 199


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    text = LINE.strip()
    if not text:
        raise SystemExit("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry is over 199 characters")
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        handle.write(text)
    if "--print" in args:
        print(text)


if __name__ == "__main__":
    main()
