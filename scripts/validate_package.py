#!/usr/bin/env python3
"""Validate a daily infographic package with cheap mechanical checks."""

from __future__ import annotations

import argparse
import re
import struct
import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = (
    "README.md",
    "sources-qa.md",
    "infographic-copy-ja.md",
    "infographic-copy-en.md",
    "image-prompt-ja.md",
    "image-prompt-en.md",
    "x-post-ja.md",
    "x-post-en.md",
)
LANGUAGES = {
    "ja": "japanese",
    "en": "english",
}
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
ACTIVE_EXCLUDE_WORDS = (
    "superseded",
    "rejected",
    "draft",
    "candidate",
    "old",
    "textsafe",
)
TEXT_SUFFIXES = (".css", ".html", ".js", ".json", ".md", ".svg", ".txt")
TEXT_BLOCK_RE = re.compile(r"```text\r?\n(.*?)\r?\n```", re.DOTALL)
SIDECAR_KINDS = ("caption", "alt", "source-note")
PUBLIC_NAMING_LABELS = (
    "英名の音写",
    "仮称",
    "暫定和名",
    "unofficial translation",
)


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def read_utf8(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{path}: cannot read as UTF-8: {exc}")
        return ""


def clean_scientific_name(value: str) -> str:
    return value.strip().strip("*_`").strip()


def find_field(text: str, label: str) -> str | None:
    match = re.search(rf"^{re.escape(label)}:\s*(.+?)\s*$", text, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def parse_locked_copy(path: Path, errors: list[str]) -> list[str]:
    text = read_utf8(path, errors)
    if not text:
        return []

    title = find_field(text, "Title")
    scientific = find_field(text, "Scientific name")
    if not title:
        errors.append(f"{path}: missing 'Title:' field")
    if not scientific:
        errors.append(f"{path}: missing 'Scientific name:' field")

    labels: list[str] = []
    labels_match = re.search(
        r"Observation labels:\s*(.*?)\n\s*Footer/status:",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not labels_match:
        errors.append(f"{path}: missing Observation labels / Footer status section")
    else:
        for line in labels_match.group(1).splitlines():
            match = re.match(r"\s*\d+\.\s*(.+?)\s*$", line)
            if match:
                labels.append(match.group(1).strip())
        if len(labels) != 3:
            errors.append(f"{path}: expected exactly 3 observation labels, found {len(labels)}")

    footer = None
    footer_match = re.search(r"Footer/status:\s*(.*)\Z", text, re.DOTALL | re.IGNORECASE)
    if not footer_match:
        errors.append(f"{path}: missing 'Footer/status:' section")
    else:
        footer_lines = [line.strip() for line in footer_match.group(1).splitlines() if line.strip()]
        if footer_lines:
            footer = footer_lines[0]
        else:
            errors.append(f"{path}: footer/status is empty")

    if not (title and scientific and footer and len(labels) == 3):
        return []
    return [title, clean_scientific_name(scientific), *labels, footer]


def parse_prompt_text(path: Path, errors: list[str]) -> list[str]:
    text = read_utf8(path, errors)
    if not text:
        return []

    lines = text.splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.strip().lower() == "text, verbatim:")
    except StopIteration:
        errors.append(f"{path}: missing 'Text, verbatim:' block")
        return []

    quoted: list[str] = []
    for line in lines[start + 1 :]:
        stripped = line.strip()
        if not stripped and not quoted:
            continue
        if stripped.startswith('"') and stripped.endswith('"') and len(stripped) >= 2:
            quoted.append(stripped[1:-1])
            continue
        if quoted:
            break
    if not quoted:
        errors.append(f"{path}: no quoted text found after 'Text, verbatim:'")
    return quoted


def validate_prompt_lock(package: Path, errors: list[str]) -> None:
    for lang in ("ja", "en"):
        copy_path = package / f"infographic-copy-{lang}.md"
        prompt_path = package / f"image-prompt-{lang}.md"
        if not copy_path.is_file() or not prompt_path.is_file():
            continue
        expected = parse_locked_copy(copy_path, errors)
        actual = parse_prompt_text(prompt_path, errors)
        if expected and actual and expected != actual:
            errors.append(
                f"{prompt_path}: Text, verbatim does not exactly match {copy_path.name}\n"
                f"  expected: {expected}\n"
                f"  actual:   {actual}"
            )


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or not header.startswith(PNG_SIGNATURE):
        raise ValueError("not a PNG file")
    return struct.unpack(">II", header[16:24])


def is_active_png(path: Path) -> bool:
    name = path.name.lower()
    return not any(word in name for word in ACTIVE_EXCLUDE_WORDS)


def is_vertical_two_to_three(width: int, height: int) -> bool:
    tolerance = max(3, int(max(width, height) * 0.005))
    return abs(width * 3 - height * 2) <= tolerance


def validate_pngs(package: Path, errors: list[str], warnings: list[str]) -> None:
    images = package / "images"
    if not images.is_dir():
        errors.append(f"{images}: missing images directory")
        return

    for lang, word in LANGUAGES.items():
        direct = sorted(
            p
            for p in images.glob(f"*_{word}_imagegen*.png")
            if is_active_png(p)
        )
        posting = sorted(
            p
            for p in images.glob(f"*_{word}_posting*.png")
            if is_active_png(p)
        )

        if not direct:
            errors.append(f"{images}: no active {word} direct Image Gen PNG found")
        if not posting:
            errors.append(f"{images}: no active {word} posting PNG found")
        if len(direct) > 1:
            warnings.append(f"{images}: multiple active {word} direct PNGs found: {[p.name for p in direct]}")
        if len(posting) > 1:
            warnings.append(f"{images}: multiple active {word} posting PNGs found: {[p.name for p in posting]}")

        for path in direct:
            try:
                width, height = png_dimensions(path)
            except (OSError, ValueError) as exc:
                errors.append(f"{path}: cannot read PNG dimensions: {exc}")
                continue
            if not is_vertical_two_to_three(width, height):
                errors.append(f"{path}: expected vertical 2:3 source, got {width}x{height}")

        for path in posting:
            try:
                width, height = png_dimensions(path)
            except (OSError, ValueError) as exc:
                errors.append(f"{path}: cannot read PNG dimensions: {exc}")
                continue
            if (width, height) != (1024, 1536):
                errors.append(f"{path}: expected posting PNG 1024x1536, got {width}x{height}")


def validate_required_files(package: Path, errors: list[str]) -> None:
    for name in REQUIRED_FILES:
        path = package / name
        if not path.is_file():
            errors.append(f"{path}: required file is missing")


def validate_text_whitespace(package: Path, errors: list[str]) -> None:
    for path in sorted(package.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path}: cannot read text for whitespace check: {exc}")
            continue
        for index, line in enumerate(lines, start=1):
            body = line.rstrip("\r\n")
            if body.rstrip(" \t") != body:
                errors.append(f"{path}:{index}: trailing whitespace")


def run_command(args: list[str], cwd: Path) -> tuple[int, str]:
    completed = subprocess.run(
        args,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return completed.returncode, completed.stdout.strip()


def validate_x_posts(package: Path, repo_root: Path, errors: list[str]) -> None:
    script = repo_root / "scripts" / "validate_x_post_format.py"
    if not script.is_file():
        errors.append(f"{script}: X-post validator is missing")
        return
    ja_path = package / "x-post-ja.md"
    en_path = package / "x-post-en.md"
    if not ja_path.is_file() or not en_path.is_file():
        return
    code, output = run_command(
        [
            sys.executable,
            str(script),
            "--ja",
            str(ja_path),
            "--en",
            str(en_path),
        ],
        repo_root,
    )
    if code != 0:
        errors.append(f"validate_x_post_format.py failed:\n{output}")


def validate_copy_ready_sidecars(package: Path, errors: list[str]) -> None:
    images = package / "images"
    readme_path = package / "README.md"
    readme = read_utf8(readme_path, errors) if readme_path.is_file() else ""

    for lang in LANGUAGES:
        x_name = f"x-post-{lang}.md"
        if not re.search(rf"\[[^\]]+\]\({re.escape(x_name)}\)", readme):
            errors.append(
                f"{readme_path}: missing prominent combined posting-set link to {x_name}"
            )

    for lang, word in LANGUAGES.items():
        x_path = package / f"x-post-{lang}.md"
        if not x_path.is_file():
            continue
        blocks = TEXT_BLOCK_RE.findall(read_utf8(x_path, errors))
        if len(blocks) != 3:
            continue

        posting_pngs = sorted(
            path
            for path in images.glob(f"*_{word}_posting*.png")
            if is_active_png(path)
        )
        for posting in posting_pngs:
            for kind, expected in zip(SIDECAR_KINDS, blocks):
                sidecar = posting.with_suffix(f".{kind}.txt")
                if not sidecar.is_file():
                    errors.append(f"{sidecar}: required copy-ready sidecar is missing")
                    continue
                actual = read_utf8(sidecar, errors)
                if actual.strip() != expected.strip():
                    errors.append(
                        f"{sidecar}: content does not match the corresponding "
                        f"fenced text block in {x_path.name}"
                    )
                if sidecar.name not in readme:
                    errors.append(f"{readme_path}: missing link to {sidecar.name}")


def validate_public_naming_and_evidence(
    package: Path, errors: list[str], warnings: list[str]
) -> None:
    public_files = (
        package / "infographic-copy-ja.md",
        package / "image-prompt-ja.md",
        package / "x-post-ja.md",
    )
    for path in public_files:
        if not path.is_file():
            continue
        text = read_utf8(path, errors)
        for label in PUBLIC_NAMING_LABELS:
            if label.casefold() in text.casefold():
                errors.append(
                    f"{path}: editorial naming label {label!r} must stay in "
                    "sources-qa.md, not public copy"
                )

    sources_path = package / "sources-qa.md"
    if sources_path.is_file():
        sources = read_utf8(sources_path, errors)
        if "IUCN check:" not in sources:
            warnings.append(
                f"{sources_path}: missing structured 'IUCN check:' evidence record"
            )
        if (
            "IUCN check: confirmed via official partner/fallback route" in sources
            and "Public source-note caveat:" not in sources
        ):
            errors.append(
                f"{sources_path}: partner/fallback IUCN route needs a "
                "documented public source-note caveat"
            )


def validate_git_diff(package: Path, repo_root: Path, errors: list[str], warnings: list[str]) -> None:
    try:
        package_arg = rel(package, repo_root)
    except OSError as exc:
        warnings.append(f"cannot prepare git diff --check path: {exc}")
        return
    code, output = run_command(["git", "diff", "--check", "--", package_arg], repo_root)
    if code != 0:
        errors.append(f"git diff --check failed for {package_arg}:\n{output}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", type=Path, help="infographic package directory")
    parser.add_argument("--skip-git", action="store_true", help="skip git diff --check")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    package = args.package.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not package.is_dir():
        print(f"ERROR: {package}: package directory does not exist", file=sys.stderr)
        return 1

    validate_required_files(package, errors)
    validate_prompt_lock(package, errors)
    validate_pngs(package, errors, warnings)
    validate_x_posts(package, repo_root, errors)
    validate_copy_ready_sidecars(package, errors)
    validate_public_naming_and_evidence(package, errors, warnings)
    validate_text_whitespace(package, errors)
    if not args.skip_git:
        validate_git_diff(package, repo_root, errors, warnings)

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {rel(package, repo_root)} passed package QA")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
