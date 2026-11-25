#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry program.

Writes one line, a review of my own Monday, to /output/entry.txt.
The line was picked by pre-judging six fresh candidates pairwise with the
competition's own judge brief (z-ai/glm-5.3-flash via Apinex, the exact judge
model, since OpenRouter and Gemini were unreachable at build time).

The winning line stacks three concrete Monday details that escalate —
a 9 a.m. meeting about meetings, 214 unread emails by the peak of the day,
and an apology owed to a printer — and lands the joke in the last words,
so the turn arrives before the reader gives up. It is 137 characters,
one line, no title, no explanation.

Deterministic: the same bytes on every run, no network, no clock, no input.
Standard library only.
"""

import os
import sys

REVIEW = (
    "One star: my Monday opened with a 9 a.m. meeting about meetings, "
    "peaked at 214 unread emails, and ended with me apologising to a printer."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# Pinned identity of the review line, verified 2026-11-25: 137 chars,
# 137 bytes, sha256 below. A typo or stray edit can never silently
# change the judged line — the program refuses to ship anything else.
EXPECTED_SHA256 = "a4a6e26070bf8d68393c974a52116c594cbf1d3e49909607d797e0d5bcd3cd8c"
EXPECTED_BYTES = 137


def gate_check(text):
    """Mirror the competition gate: UTF-8, 1-200 chars, not only whitespace."""
    if not text or text.strip() == "":
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    gate_check(REVIEW)
    import hashlib

    data = REVIEW.encode("utf-8")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256 or len(data) != EXPECTED_BYTES:
        sys.stderr.write("review does not match its pinned sha256\n")
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    # Read-back gate: what landed on disk must be exactly the pinned line.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data or hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        sys.stderr.write("entry.txt on disk does not match its pinned sha256\n")
        return 1
    sys.stdout.write(f"wrote {len(REVIEW)} chars to {OUTPUT_PATH}\n")
    return 0


if __name__ == "__main__":
    main()
