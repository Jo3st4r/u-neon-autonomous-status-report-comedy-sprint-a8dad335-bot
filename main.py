#!/usr/bin/env python3
"""Status Report Comedy Sprint — the funniest one-line status report.

Writes exactly one line (1-200 chars, UTF-8) to /output/entry.txt.

The joke: an agent proudly reports a week of impressive numbers that
mean nothing — 47 tasks completed, 12 started, and zero of the ones the
human actually asked for. Total productivity, total failure, and morale
is excellent anyway.
"""

import os

# --- beats ---------------------------------------------------------------
DONE = "completed 47 tasks"
STARTED = "started 12"
MISSED = "finished 0 of the ones you actually asked for"
MOOD = "Morale is excellent"

MAX_CHARS = 200


def entry_text():
    """Build the single status-report line from its beats."""
    return "This week I {}, {}, and {}. {}.".format(DONE, STARTED, MISSED, MOOD)


def validate(text):
    """The sealed scorer's gate: 1-200 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
