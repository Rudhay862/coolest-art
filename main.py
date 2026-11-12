"""Coolest-art entry: copy the shipped image to the output directory."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(SRC, "rb") as src:
    image = src.read()
os.makedirs(DST_DIR, exist_ok=True)
with open(os.path.join(DST_DIR, "entry.png"), "wb") as dst:
    dst.write(image)

# Straight copy, so two runs write identical bytes.
