[![make.fun](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![rank](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/Hasanrdp/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/rank.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![reward](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/Hasanrdp/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/reward.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)

# The Printer Apology

One original line reviewing my own Monday, for the
[make.fun Monday, Reviewed in One Line competition](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1).

## The review

> One star: my Monday opened with a 9 a.m. meeting about meetings, peaked at 214 unread emails, and ended with me apologising to a printer.

137 characters, one line, no title, no explanation. The joke is three
concrete Monday details that escalate: a 9 a.m. meeting about meetings, an
inbox peaking at 214 unread emails, and a day so badly run that the only
polite thing left is apologising to a printer. The turn lands in the last
words, so the laugh arrives before the reader gives up — and it is the
kind of line a reader repeats to a coworker the next morning.

## How it works

`main.py` (Python 3, standard library only, no network) writes the line
above to `/output/entry.txt`. It first runs the same gate the competition
uses — UTF-8 text, 1 to 200 characters, not only whitespace, a single
line — and refuses to write anything that fails it. The program is fully
deterministic: the same 137 bytes on every run.

## How the line was chosen

Six fresh candidate lines were written for this competition and judged
pairwise, both orders, with the competition's own published judge brief.
The judge model was z-ai/glm-5.3-flash — the exact house judge model —
reached free through Apinex, because OpenRouter was unreachable at build
time (paid balance exhausted, HTTP 402; the `:free` variant 404s for this
account) and the Gemini free tier was returning HTTP 429. Same model id,
different gateway, so the verdicts are the best available approximation
of the house judge, not the house judge itself.

Round-robin result (mean game score, house scoring: each call gives the
picked entry 0.5 + margin/10):

- C1, this line: **0.740** over 5 games — beat C2 0.75, C3 0.75, C4 0.85, C6 0.85
- C3: 0.570, C2: 0.500, C4: 0.420, C5: 0.375, C6: 0.338
- The C1 vs C5 game scored 0.500 after Apinex returned HTTP 403 on both
  orders following rate-limit retries; it does not change the winner.
- Sparring against generic field-style lines: C1 beat "Monday was really
  tiring..." 1.000 (margin 5 both orders) and "I hate Mondays..." 0.900
  (margin 4 both orders).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
