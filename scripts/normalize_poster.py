"""Validate a 2:3 poster and resize it to the series' 1024x1536 delivery size."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


DEFAULT_SIZE = (1024, 1536)
MAX_ASPECT_ERROR = 0.005


def parse_size(value: str) -> tuple[int, int]:
    try:
        width, height = (int(part) for part in value.lower().split("x", 1))
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("size must look like 1024x1536") from exc
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("size dimensions must be positive")
    return width, height


def aspect_error(source: tuple[int, int], target: tuple[int, int]) -> float:
    source_width, source_height = source
    target_width, target_height = target
    expected_width = source_height * target_width / target_height
    return abs(source_width - expected_width) / expected_width


def normalize(
    source: Path,
    output: Path,
    size: tuple[int, int],
) -> None:
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        error = aspect_error(image.size, size)
        if error > MAX_ASPECT_ERROR:
            raise ValueError(
                f"{source} is {image.width}x{image.height}, not vertical 2:3 "
                f"(aspect error {error:.2%}). Regenerate the poster; padding, "
                "cropping, and stretching are not allowed."
            )
        resized = image.resize(size, Image.Resampling.LANCZOS)

    output.parent.mkdir(parents=True, exist_ok=True)
    resized.save(output, format="PNG", optimize=True)

    with Image.open(output) as result:
        if result.size != size:
            raise RuntimeError(
                f"unexpected output size: {result.size}; expected {size}"
            )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Reject posters that are not already vertical 2:3, then resize "
            "accepted posters to the fixed delivery dimensions. No padding, "
            "cropping, or material aspect-ratio correction is used."
        )
    )
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--size", type=parse_size, default=DEFAULT_SIZE)
    args = parser.parse_args()

    try:
        normalize(args.input, args.output, args.size)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc


if __name__ == "__main__":
    main()
