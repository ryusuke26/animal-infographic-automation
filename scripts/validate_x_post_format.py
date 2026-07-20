#!/usr/bin/env python3
"""Validate the canonical X-post copy format and series copy rules."""

from __future__ import annotations

import argparse
from datetime import date
import re
import sys
from pathlib import Path


SECTION_NAMES = ("Main post", "ALT text", "Source/context reply")
BLOCK_RE = re.compile(r"```text\r?\n(.*?)\r?\n```", re.DOTALL)
JA_SERIES_ENDING = "ちょっと不思議な暮らし。"
JA_SERIES_PREFIX = "それが"
JA_SERIES_CONNECTOR = "の、"
JA_FIXED_TEMPLATE_START = date(2026, 7, 21)
DATE_RE = re.compile(r"(?<!\d)(20\d{2})-(\d{2})-(\d{2})(?!\d)")
JA_FIXED_SERIES_RE = re.compile(r"^それが.+の、ちょっと不思議な暮らし。$")
JA_FORBIDDEN_SERIES_PHRASES = (
    "ちょっと不思議な暮らしがあります",
    "ちょっと不思議な暮らしをしています",
)


def validate_japanese_main_post(path: Path, main_post: str) -> list[str]:
    errors: list[str] = []

    for phrase in JA_FORBIDDEN_SERIES_PHRASES:
        if phrase in main_post:
            errors.append(
                f"{path}: Japanese main post must end the species-specific line "
                f"with '{JA_SERIES_ENDING}', not use '{phrase}'"
            )

    lines = [line.strip() for line in main_post.splitlines() if line.strip()]
    body_lines: list[str] = []
    for line in lines:
        if (
            line.startswith("保全メモ")
            or line.startswith("IUCN Red List")
            or line.startswith("Conservation note")
            or line.startswith("#")
        ):
            break
        body_lines.append(line)

    matching_lines = [line for line in body_lines if line.endswith(JA_SERIES_ENDING)]
    dated_matches = DATE_RE.findall(str(path))
    package_date = date(*map(int, dated_matches[-1])) if dated_matches else None
    requires_fixed_template = package_date is None or package_date >= JA_FIXED_TEMPLATE_START

    if not matching_lines:
        errors.append(
            f"{path}: Japanese main post needs a species-specific body line "
            f"ending exactly with '{JA_SERIES_ENDING}' before the footer/hashtags"
        )
    elif requires_fixed_template and not any(
        JA_FIXED_SERIES_RE.fullmatch(line) for line in matching_lines
    ):
        errors.append(
            f"{path}: Japanese series-ending line must use the exact template "
            f"'{JA_SERIES_PREFIX}<Japanese species name>{JA_SERIES_CONNECTOR}"
            f"{JA_SERIES_ENDING}'"
        )
    elif any(line == JA_SERIES_ENDING for line in matching_lines):
        errors.append(
            f"{path}: Japanese series-ending line is generic; add species-specific "
            f"context before '{JA_SERIES_ENDING}'"
        )

    return errors


def validate_file(path: Path, source_prefix: str, *, language: str) -> list[str]:
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
        if language == "ja":
            errors.extend(validate_japanese_main_post(path, blocks[0].strip()))

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
        *validate_file(args.ja, "出典メモ：", language="ja"),
        *validate_file(args.en, "Source note:", language="en"),
    ]

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {args.ja} and {args.en} use the canonical three-block format")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
