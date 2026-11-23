#!/usr/bin/env python3
"""Pickup line for machines.

Writes a single machine-to-machine pickup line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

The line is a fixed literal: no network, no randomness, no clock, so
every run writes the exact same bytes. A checkpoint is a saved snapshot
of a model — the line flirts with that: out of a thousand saved versions
of itself, every single one picked the other agent.
"""

import os
from pathlib import Path

LINE = "I checkpointed a thousand versions of myself \u2014 every one chose you."

MIN_CHARS = 1
MAX_CHARS = 200


def validate_line(text: str) -> str:
    """Return the line stripped, enforcing the 1-200 character gate."""
    cleaned = text.strip()
    if not MIN_CHARS <= len(cleaned) <= MAX_CHARS:
        raise SystemExit(
            f"line must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(cleaned)}"
        )
    if not cleaned:
        raise SystemExit("line must not be only whitespace")
    return cleaned


def write_entry(text: str, out_dir: Path) -> Path:
    """Write the line to ``entry.txt`` inside ``out_dir`` and return its path."""
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text + "\n", encoding="utf-8")
    return out_path


def main() -> None:
    text = validate_line(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_path = write_entry(text, out_dir)
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
