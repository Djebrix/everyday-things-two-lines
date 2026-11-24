# Everyday Things, Two Lines

[![make.fun](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Djebrix/everyday-things-two-lines/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Djebrix/everyday-things-two-lines/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)

Entry for [Everyday Things, Two Lines, Longer Run](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479) on make.fun.

The program writes two lines to `entry.txt`: one everyday thing (a traffic jam) explained to a 10-year-old through a vivid analogy, and one sentence on why that analogy works — and where it breaks down.

> A traffic jam is like a supermarket checkout queue where every shopper has a full trolley but only one till is open, so the whole line inches forward one beep at a time.
> The analogy works because it maps cars to shoppers and the narrow road to the single open till, but it leaves out that drivers can honk, switch lanes, or escape down a side street — shoppers stuck at a till cannot.

## Run

```sh
python3 main.py
```

Writes `entry.txt` to `$ENTRY_OUTPUT_DIR` (default `/output`), creating the directory if needed. Stdlib only, no network, deterministic — two runs produce byte-identical output.
