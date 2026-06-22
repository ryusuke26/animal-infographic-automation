#!/usr/bin/env python3
"""Validate the canonical three-block X-post copy format."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SECTION_NAMES = ("Main post", "ALT text", "Source/context reply")
BLOCK_RE = re.compile(r"```text\r?\n(.*?)\r?\n```", re.DOTALL)


def validate_file(path: Path, source_prefix: str) -> list[str]:
    errors: list[str] = []

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{path}: cannot read as UTF-8: {exc}"]

    blocks = BLOCK_RE.findall(text)
    if len(blocks) != 3:
        errors.append(
            f"{path}: expected exactly 3 fenced text blocks, found {len(blocks)}"
        )

    heading_positions: list[int] = []
    for name in SECTION_NAMES:
        marker = f"## {name}"
        count = text.count(marker)
        if count != 1:
            errors.append(f"{path}: expected one '{marker}' heading, found {count}")
        heading_positions.append(text.find(marker))

    if all(position >= 0 for position in heading_positions) and heading_positions != sorted(
        heading_positions
    ):
        errors.append(f"{path}: section headings are out of order")

    for name, block in zip(SECTION_NAMES, blocks):
        if not block.strip():
            errors.append(f"{path}: '{name}' block is empty")

    if len(blocks) == 3:
        source_note = blocks[2].strip()
        if not source_note.startswith(source_prefix):
            errors.append(
                f"{path}: source block must begin exactly with '{source_prefix}'"
            )
        if "https://" not in source_note:
            errors.append(f"{path}: source block has no direct HTTPS link")

        for name, start, end in zip(
            SECTION_NAMES,
            heading_positions,
            heading_positions[1:] + [len(text)],
        ):
            if start < 0:
                continue
            section = text[start:end]
            if len(BLOCK_RE.findall(section)) != 1:
                errors.append(
                    f"{path}: '{name}' must contain exactly one fenced text block"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ja", required=True, type=Path)
    parser.add_argument("--en", required=True, type=Path)
    args = parser.parse_args()

    errors = [
        *validate_file(args.ja, "出典メモ："),
        *validate_file(args.en, "Source note:"),
    ]

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {args.ja} and {args.en} use the canonical three-block format")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
