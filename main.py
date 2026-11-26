#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence (make.fun u-kiencx-out-of-tokens-mid-sentence-00f60233).

The entry is one funny error line an AI agent shows when it runs out of
tokens mid-sentence, written to /output/entry.txt. The line is a constant
in this file, so two runs always produce identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LINE = (
    "Error: token limit reached. The rest of this sentence has been "
    "outsourced to your imagination, free of charge."
)

_OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
_DST = os.path.join(_OUT_DIR, "entry.txt")


def main() -> None:
    # Competition limits: 1-140 UTF-8 characters, not only whitespace.
    # Validate the constant before writing anything. The gate counts the
    # text; the trailing newline below keeps the file at 111 characters,
    # still inside the limit, and the byte count (110) is what the
    # leaderboard's size tie-break reads.
    if not LINE.strip():
        raise SystemExit("line is empty or only whitespace")
    if len(LINE) > 140:
        raise SystemExit(f"line is {len(LINE)} characters, over the 140 limit")
    if len(LINE.encode("utf-8")) > 140:
        raise SystemExit("line is over 140 bytes")
    os.makedirs(_OUT_DIR, exist_ok=True)
    with open(_DST, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
