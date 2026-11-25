"""Worst App Idea entry: copy the one-line pitch from entry.txt to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The entry text lives in entry.txt next to this script; this
program only moves it to the grader's output directory, unchanged.
"""

import os
from pathlib import Path


def main():
    try:
        src = Path(__file__).resolve().parent / "entry.txt"
        text = src.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise SystemExit(f"cannot read entry.txt: {exc}") from exc
    if not text.strip():
        raise SystemExit("entry.txt is empty")
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
