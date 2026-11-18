"""Solmar Bay newspaper entry — copy entry.png into the output directory.

The entry is a single pre-rendered image (a newspaper front page). This
program does the one thing the competition harness needs: it places a copy
of entry.png in the output directory, which is the directory named by the
MAKEFUN_OUTPUT_DIR environment variable, or /output when that is unset.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print(f"error: {src} not found", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copy(src, dst)
    print(f"copied {src} -> {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
