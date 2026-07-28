#!/usr/bin/env python3
"""Validate the canonical X-post copy format and series copy rules."""

from __future__ import annotations

import argparse
from datetime import date
import re
import sys
from pathlib import Path


LEGACY_SECTION_NAMES = ("Main post", "ALT text", "Source/context reply")
STORY_SECTION_NAMES = (
    "Main post",
    "Story reply",
    "ALT text",
    "Source/context reply",
)
BLOCK_RE = re.compile(r"```text\r?\n(.*?)\r?\n```", re.DOTALL)
JA_SERIES_ENDING = "ちょっと不思議な暮らし。"
JA_SERIES_PREFIX = "それが"
JA_SERIES_CONNECTOR = "の、"
JA_FIXED_TEMPLATE_START = date(2026, 7, 21)
IDENTITY_SEQUENCE_START = date(2026, 7, 24)
MAIN_POST_LENGTH_START = date(2026, 7, 28)
ENGLISH_HASHTAG_START = date(2026, 7, 28)
STORY_REPLY_START = date(2026, 7, 28)
MAX_MAIN_POST_CHARACTERS = 275
DATE_RE = re.compile(r"(?<!\d)(20\d{2})-(\d{2})-(\d{2})(?!\d)")
JA_FIXED_SERIES_RE = re.compile(r"^それが.+の、ちょっと不思議な暮らし。$")
JA_FORBIDDEN_SERIES_PHRASES = (
    "ちょっと不思議な暮らしがあります",
    "ちょっと不思議な暮らしをしています",
)


def package_date_for(path: Path) -> date | None:
    dated_matches = DATE_RE.findall(str(path))
    return date(*map(int, dated_matches[-1])) if dated_matches else None


def section_names_for(path: Path) -> tuple[str, ...]:
    package_date = package_date_for(path)
    if package_date is None or package_date >= STORY_REPLY_START:
        return STORY_SECTION_NAMES
    return LEGACY_SECTION_NAMES


def validate_identity_sequence(path: Path, main_post: str, language: str) -> list[str]:
    errors: list[str] = []
    package_date = package_date_for(path)
    if package_date is not None and package_date < IDENTITY_SEQUENCE_START:
        return errors

    copy_path = path.parent / f"infographic-copy-{language}.md"
    if not copy_path.is_file():
        return errors

    try:
        locked_copy = copy_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{copy_path}: cannot read as UTF-8: {exc}"]

    title_match = re.search(r"^Title:\s*(.+?)\s*$", locked_copy, re.MULTILINE)
    scientific_match = re.search(
        r"^Scientific name:\s*(.+?)\s*$", locked_copy, re.MULTILINE
    )
    if not title_match or not scientific_match:
        return [f"{copy_path}: cannot read locked title/scientific name"]

    title = title_match.group(1).strip().strip("*`")
    scientific_name = scientific_match.group(1).strip().strip("*`")
    lines = [line.strip() for line in main_post.splitlines() if line.strip()]
    sequence_positions = [
        index
        for index in range(len(lines) - 1)
        if lines[index] == title and lines[index + 1] == scientific_name
    ]

    if len(sequence_positions) != 1:
        errors.append(
            f"{path}: main post must contain exactly one adjacent standalone "
            f"identity sequence '{title}' then '{scientific_name}'"
        )
    elif sequence_positions[0] == 0:
        errors.append(
            f"{path}: main post needs a species-specific hook before the "
            "standalone common/scientific name lines"
        )

    return errors


def validate_post_length(path: Path, post: str, label: str) -> list[str]:
    package_date = package_date_for(path)
    if package_date is not None and package_date < MAIN_POST_LENGTH_START:
        return []

    character_count = len(post)
    if character_count > MAX_MAIN_POST_CHARACTERS:
        return [
            f"{path}: {label} is {character_count} characters; new packages "
            f"must stay at or below {MAX_MAIN_POST_CHARACTERS}"
        ]

    return []


def validate_english_name_hashtag(path: Path, main_post: str) -> list[str]:
    package_date = package_date_for(path)
    if package_date is not None and package_date < ENGLISH_HASHTAG_START:
        return []

    copy_path = path.parent / "infographic-copy-en.md"
    if not copy_path.is_file():
        return []

    try:
        locked_copy = copy_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{copy_path}: cannot read as UTF-8: {exc}"]

    title_match = re.search(r"^Title:\s*(.+?)\s*$", locked_copy, re.MULTILINE)
    if not title_match:
        return [f"{copy_path}: cannot read locked English title"]

    title = title_match.group(1).strip().strip("*`")
    hashtag = "#" + "".join(re.findall(r"[A-Za-z0-9]+", title))
    if hashtag == "#":
        return [f"{copy_path}: cannot derive English-name hashtag from '{title}'"]

    count = len(re.findall(rf"(?<!\w){re.escape(hashtag)}(?!\w)", main_post))
    if count != 1:
        return [
            f"{path}: main post must contain exactly one English-name hashtag "
            f"'{hashtag}', found {count}"
        ]

    return []


def validate_short_main_structure(
    path: Path, main_post: str, language: str
) -> list[str]:
    copy_path = path.parent / f"infographic-copy-{language}.md"
    if not copy_path.is_file():
        return []

    try:
        locked_copy = copy_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{copy_path}: cannot read as UTF-8: {exc}"]

    title_match = re.search(r"^Title:\s*(.+?)\s*$", locked_copy, re.MULTILINE)
    scientific_match = re.search(
        r"^Scientific name:\s*(.+?)\s*$", locked_copy, re.MULTILINE
    )
    footer_match = re.search(
        r"^Footer/status:\s*\r?\n([^\r\n]+)", locked_copy, re.MULTILINE
    )
    if not title_match or not scientific_match or not footer_match:
        return [f"{copy_path}: cannot read locked title/scientific name/footer"]

    title = title_match.group(1).strip().strip("*`")
    scientific_name = scientific_match.group(1).strip().strip("*`")
    footer = footer_match.group(1).strip()
    lines = [line.strip() for line in main_post.splitlines() if line.strip()]
    try:
        identity_index = next(
            index
            for index in range(len(lines) - 1)
            if lines[index] == title and lines[index + 1] == scientific_name
        )
    except StopIteration:
        return []

    trailing_lines = lines[identity_index + 2 :]
    if trailing_lines.count(footer) != 1:
        return [
            f"{path}: short main post must contain the locked footer exactly once"
        ]

    unexpected = [
        line for line in trailing_lines if line != footer and not line.startswith("#")
    ]
    if unexpected:
        return [
            f"{path}: fuller natural-history copy belongs in 'Story reply', "
            f"not after the identity lines in 'Main post': {unexpected[0]!r}"
        ]

    return []


def validate_japanese_story_reply(path: Path, story_reply: str) -> list[str]:
    errors: list[str] = []

    for phrase in JA_FORBIDDEN_SERIES_PHRASES:
        if phrase in story_reply:
            errors.append(
                f"{path}: Japanese story reply must end the species-specific line "
                f"with '{JA_SERIES_ENDING}', not use '{phrase}'"
            )

    lines = [line.strip() for line in story_reply.splitlines() if line.strip()]
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
    package_date = package_date_for(path)
    requires_fixed_template = package_date is None or package_date >= JA_FIXED_TEMPLATE_START

    if not matching_lines:
        errors.append(
            f"{path}: Japanese story reply needs a species-specific body line "
            f"ending exactly with '{JA_SERIES_ENDING}'"
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

    if len(body_lines) < 2:
        errors.append(
            f"{path}: Japanese story reply needs narrative copy before the "
            "series-ending line"
        )

    return errors


def validate_file(path: Path, source_prefix: str, *, language: str) -> list[str]:
    errors: list[str] = []

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{path}: cannot read as UTF-8: {exc}"]

    section_names = section_names_for(path)
    expected_block_count = len(section_names)
    blocks = BLOCK_RE.findall(text)
    if len(blocks) != expected_block_count:
        errors.append(
            f"{path}: expected exactly {expected_block_count} fenced text blocks, "
            f"found {len(blocks)}"
        )

    heading_positions: list[int] = []
    for name in section_names:
        marker = f"## {name}"
        count = text.count(marker)
        if count != 1:
            errors.append(f"{path}: expected one '{marker}' heading, found {count}")
        heading_positions.append(text.find(marker))

    if all(position >= 0 for position in heading_positions) and heading_positions != sorted(
        heading_positions
    ):
        errors.append(f"{path}: section headings are out of order")

    for name, block in zip(section_names, blocks):
        if not block.strip():
            errors.append(f"{path}: '{name}' block is empty")

    if len(blocks) == expected_block_count:
        main_post = blocks[0].strip()
        errors.extend(validate_post_length(path, main_post, "main post"))
        errors.extend(validate_identity_sequence(path, main_post, language))
        errors.extend(validate_english_name_hashtag(path, main_post))

        has_story_reply = section_names == STORY_SECTION_NAMES
        story_reply = blocks[1].strip() if has_story_reply else main_post
        if has_story_reply:
            errors.extend(validate_post_length(path, story_reply, "story reply"))
            errors.extend(validate_short_main_structure(path, main_post, language))
            if JA_SERIES_ENDING in main_post:
                errors.append(
                    f"{path}: Japanese series ending belongs in the story reply, "
                    "not the main post"
                )
            if any(
                line.strip().startswith(
                    ("IUCN Red List", "Conservation note", "保全メモ", "#")
                )
                for line in story_reply.splitlines()
            ):
                errors.append(
                    f"{path}: status footer and hashtags belong in the main post, "
                    "not the story reply"
                )
        if language == "ja":
            errors.extend(validate_japanese_story_reply(path, story_reply))

        source_note = blocks[-1].strip()
        if not source_note.startswith(source_prefix):
            errors.append(
                f"{path}: source block must begin exactly with '{source_prefix}'"
            )
        if "https://" not in source_note:
            errors.append(f"{path}: source block has no direct HTTPS link")

        for name, start, end in zip(
            section_names,
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

    print(f"OK: {args.ja} and {args.en} use the canonical posting-set format")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
