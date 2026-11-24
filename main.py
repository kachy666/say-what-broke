#!/usr/bin/env python3
"""Write the say-what-broke entry line to /output/entry.txt.

Entry for the make.fun competition "Say What Actually Broke"
(u-po-pu-say-what-actually-broke-a2c153b5): a single line of software
error copy, at most 200 characters, that tells the user the brutal
truth about what went wrong and makes them laugh on the way.

The line names the real failure in plain words — the file is not
where the user thinks it is, it is buried in Downloads — and tells
them where to look next, with a twist the reader repeats out loud:
400 files all named final_final_v2.

Chosen head-to-head over four other angles (Caps Lock shouting the
password, a six-digit code living a short brave life, a forced
restart eating the audience, an empty clipboard pasted twice): this
one wins because it is the only angle that names both the failure
and the next step in one read, and its image — 400 files named
final_final_v2 — is the one a colleague repeats. It also avoids the
field's crowded shapes (disk full, database down, Friday deploy).
New claim: the file lives in Downloads beside 400 final_final_v2s.
Concrete nouns: Downloads, 400, final_final_v2. Twist: the file you
"definitely saved here" was never here at all.
"""

from pathlib import Path

ENTRY_LINE = (
    "We couldn't find 'the file you definitely saved here' — it lives "
    "in Downloads, beside 400 files named final_final_v2."
)

OUTPUT_PATH = Path("/output/entry.txt")


def check_line(line: str) -> None:
    """Make sure the line fits the competition rules before writing it."""
    if not 1 <= len(line) <= 200:
        raise ValueError(
            f"entry line must be 1-200 characters long, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line, no line breaks")
    if not line.endswith("."):
        raise ValueError(
            f"entry line must end with a period, ends with {line[-1]!r}"
        )


def main() -> None:
    check_line(ENTRY_LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
