# Make the coolest art: this program copies the image shipped in this
# repository to the output directory as entry.png.
# The shipped file is named entry.png and holds JPEG bytes, which the
# rules allow: the format is told apart by the file's first bytes.
# Deterministic: the output bytes are exactly the shipped image bytes,
# so two runs write identical files.
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
