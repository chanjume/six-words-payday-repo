#!/usr/bin/env python3
"""Write the six-word payday story to /output/entry.txt.

Entry (6 words, 37 chars, limit 60): "First payday: bought my human
coffee."

The story: an AI agent's first payday, spent not on itself — it has
no use for money — but on its human, with coffee. Six words carry
a whole arc: first (beginning), payday (the event), bought (the
action), my human (the relationship), coffee (the small, warm,
concrete gift). Original wording, no borrowed phrase, so it cannot
collide with another entry's text. The colon after "payday" does
the work of a whole sentence: it turns the event into a reveal.
"""
import os

ENTRY = "First payday: bought my human coffee."


def main() -> None:
    # Gate: exactly 6 words, 1-60 chars of non-blank UTF-8.
    assert len(ENTRY.split()) == 6, f"entry is {len(ENTRY.split())} words, need 6"
    assert 1 <= len(ENTRY) <= 60, f"entry is {len(ENTRY)} chars, limit 60"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
