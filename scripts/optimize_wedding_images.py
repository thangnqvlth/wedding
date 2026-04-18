#!/usr/bin/env python3
"""Resize wedding JPEGs for web and emit WebP + optimized JPEG (same basename)."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
WEDDING = ROOT / "wedding"


def long_edge_cap(path: Path) -> int:
    """Hero background needs a bit more pixels; album shots cap lower."""
    if path.name == "main.jpg":
        return 2200
    return 1680


def fit_long_edge(im: Image.Image, cap: int) -> Image.Image:
    w, h = im.size
    long = max(w, h)
    if long <= cap:
        return im
    scale = cap / long
    nw = max(1, int(round(w * scale)))
    nh = max(1, int(round(h * scale)))
    return im.resize((nw, nh), Image.Resampling.LANCZOS)


def main() -> int:
    if not WEDDING.is_dir():
        print("missing wedding/", file=sys.stderr)
        return 1

    jpegs = sorted(WEDDING.glob("*.jpg"))
    if not jpegs:
        print("no jpg in wedding/", file=sys.stderr)
        return 1

    for path in jpegs:
        cap = long_edge_cap(path)
        im = Image.open(path)
        if im.mode not in ("RGB", "L"):
            im = im.convert("RGB")
        elif im.mode == "L":
            im = im.convert("RGB")

        out = fit_long_edge(im, cap)

        webp_path = path.with_suffix(".webp")
        out.save(
            webp_path,
            "WEBP",
            quality=88,
            method=6,
        )

        out.save(
            path,
            "JPEG",
            quality=88,
            optimize=True,
            progressive=True,
            subsampling=1,
        )

        print(f"{path.name}: {im.size} -> {out.size} | webp+jpeg written")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
