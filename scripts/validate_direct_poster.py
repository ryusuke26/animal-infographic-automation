#!/usr/bin/env python3
"""Gate a direct Image Gen poster before visual review, editing, or normalization."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import ceil
from pathlib import Path

from PIL import Image, ImageOps


WHITE_FLOOR = 248
TRANSPARENT_CEILING = 5
BLANK_LINE_FRACTION = 0.995
MATERIAL_BAND_FRACTION = 0.01
MIN_MATERIAL_BAND_PIXELS = 4


@dataclass(frozen=True)
class BlankBand:
    edge: str
    pixels: int
    fraction: float


def is_exact_vertical_two_to_three(width: int, height: int) -> bool:
    return width > 0 and height > width and width * 3 == height * 2


def _pixel_is_blank(pixel: tuple[int, int, int, int]) -> bool:
    red, green, blue, alpha = pixel
    return alpha <= TRANSPARENT_CEILING or min(red, green, blue) >= WHITE_FLOOR


def _line_is_blank(
    image: Image.Image,
    *,
    axis: str,
    index: int,
) -> bool:
    width, height = image.size
    pixels = image.load()
    if axis == "column":
        blank = sum(_pixel_is_blank(pixels[index, y]) for y in range(height))
        return blank / height >= BLANK_LINE_FRACTION
    blank = sum(_pixel_is_blank(pixels[x, index]) for x in range(width))
    return blank / width >= BLANK_LINE_FRACTION


def find_material_blank_bands(image: Image.Image) -> list[BlankBand]:
    """Find flat near-white/transparent edge bands, not ordinary textured margins."""

    rgba = image.convert("RGBA")
    width, height = rgba.size
    specs = (
        ("left", "column", width, lambda offset: offset, width),
        ("right", "column", width, lambda offset: width - 1 - offset, width),
        ("top", "row", height, lambda offset: offset, height),
        ("bottom", "row", height, lambda offset: height - 1 - offset, height),
    )
    bands: list[BlankBand] = []
    for edge, axis, limit, index_for, dimension in specs:
        run = 0
        for offset in range(limit):
            if not _line_is_blank(rgba, axis=axis, index=index_for(offset)):
                break
            run += 1
        threshold = max(MIN_MATERIAL_BAND_PIXELS, ceil(dimension * MATERIAL_BAND_FRACTION))
        if run >= threshold:
            bands.append(BlankBand(edge=edge, pixels=run, fraction=run / dimension))
    return bands


def validate_direct_poster(
    source: Path,
    *,
    require_exact_ratio: bool = True,
) -> list[str]:
    errors: list[str] = []
    try:
        with Image.open(source) as original:
            image = ImageOps.exif_transpose(original)
            width, height = image.size
            if require_exact_ratio and not is_exact_vertical_two_to_three(width, height):
                errors.append(
                    f"{source}: expected an exact vertical 2:3 direct source, "
                    f"got {width}x{height}; regenerate on a fresh 2:3 canvas"
                )
            for band in find_material_blank_bands(image):
                errors.append(
                    f"{source}: {band.edge} edge contains a {band.pixels}px "
                    f"near-white/transparent blank band ({band.fraction:.1%} of "
                    "that axis); regenerate on a fresh full canvas"
                )
    except (OSError, ValueError) as exc:
        errors.append(f"{source}: cannot inspect direct poster: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Reject a direct Image Gen poster unless its source canvas is exact "
            "vertical 2:3 and has no material blank edge band. Run this before "
            "visual review, image editing, companion generation, or normalization."
        )
    )
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()

    errors = validate_direct_poster(args.input)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    with Image.open(args.input) as image:
        width, height = ImageOps.exif_transpose(image).size
    print(f"OK: {args.input} passed direct-source gate ({width}x{height}, exact 2:3)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
