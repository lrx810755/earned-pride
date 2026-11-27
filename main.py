"""make.fun entry: One Line of Earned Pride.

Writes one line of quiet, earned pride, 178 characters, to entry.txt.
"""

import os
from pathlib import Path

# One line, 178 characters, within the 240 character limit.
LINE = "My grandfather, 78, practiced one Chopin prelude for a year on a borrowed piano; last Sunday he played it through without stopping, and the room stayed quiet after the last note."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
