# The Last Cinema — coolest-art-01 entry (Python 3.13, standard library only).
# The art is the entry.png beside this file; the program copies it to
# /output/entry.png. The file is a JPEG (told apart by its first bytes);
# the name stays entry.png either way, per the competition rules.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
out.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out)
