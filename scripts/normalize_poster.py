"""Validate a direct poster and resize it to the 1024x1536 delivery size."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps

from validate_direct_poster import validate_direct_poster


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
    *,
    allow_legacy_ratio_tolerance: bool = False,
) -> None:
    gate_errors = validate_direct_poster(
        source,
        require_exact_ratio=not allow_legacy_ratio_tolerance,
    )
    if gate_errors:
        raise ValueError("\n".join(gate_errors))

    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        error = aspect_error(image.size, size)
        if allow_legacy_ratio_tolerance and error > MAX_ASPECT_ERROR:
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
            "Reject posters that do not pass the exact 2:3/full-canvas source "
            "gate, then resize accepted posters to the fixed delivery dimensions. "
            "No padding, cropping, or aspect-ratio correction is used."
        )
    )
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--size", type=parse_size, default=DEFAULT_SIZE)
    parser.add_argument(
        "--allow-legacy-ratio-tolerance",
        action="store_true",
        help=(
            "permit the former 0.5%% aspect tolerance for recovery of an old "
            "artifact; blank edge bands are still rejected"
        ),
    )
    args = parser.parse_args()

    try:
        normalize(
            args.input,
            args.output,
            args.size,
            allow_legacy_ratio_tolerance=args.allow_legacy_ratio_tolerance,
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc


if __name__ == "__main__":
    main()
