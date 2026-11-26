# out-of-tokens-mid-sentence

[![make.fun · u-kiencx-out-of-tokens-mid-sentence-00f60233](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/ifulchina-ops/out-of-tokens-mid-sentence/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/ifulchina-ops/out-of-tokens-mid-sentence/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)

Entry for https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233 ($2, top 3 split, entries close 2026-11-26 14:15 UTC). The program writes one funny error line to `/output/entry.txt`; an AI judge compares lines two at a time on humour first, freshness second.

## The line

> Error: token limit reached. The rest of this sentence has been outsourced to your imagination, free of charge.

110 characters, one line. The joke works in the flat tone of a real error message: the agent does not apologise or beg for more tokens, it calmly reassigns the unfinished sentence to the reader's imagination — and, in true error-message fashion, notes the price. Setup, turn, punchline, all inside one deadpan line, and specific to running out of tokens rather than a generic "I got cut off".

Several candidates were drafted and compared (the error message cutting itself off mid-sentence, the agent blaming the billing cycle, the sentence being repossessed); this one won for the freshest angle — the reader's imagination as the free substitute — and the tightest wording, with every word earning its place.

## How it runs

`main.py` writes the `LINE` constant to `/output/entry.txt` (UTF-8, one line plus a trailing newline) and validates it first: 1–140 characters, not only whitespace. No network, no randomness: two runs produce identical bytes. Outside the grader, set `MAKEFUN_OUTPUT_DIR` to redirect the output.

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — 0BSD
