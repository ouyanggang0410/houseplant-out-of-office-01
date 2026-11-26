"""Write one original houseplant out-of-office reply to entry.txt.

Written fresh for the make.fun "The Houseplant Out-of-Office"
bounty. The program takes no input, makes no network calls, and
writes exactly one line of UTF-8 text (1-120 characters).
"""

import os
from pathlib import Path

LINE = "Out of office: the fern by the window. Unwatered since March, I've started photosynthesizing resentment instead."


def output_path() -> Path:
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    base = Path(override) if override else Path("/output")
    return base / "entry.txt"


def main() -> None:
    # The gate allows 1-120 characters; fail loudly instead of
    # writing an entry the judge would never see.
    assert 1 <= len(LINE) <= 120, "entry line must be 1-120 characters"
    assert "\n" not in LINE, "entry must be a single line"
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
