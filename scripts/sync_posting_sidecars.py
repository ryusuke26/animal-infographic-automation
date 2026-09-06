"""Derive copy-ready sidecars from validated X files; read-only unless --write."""

import argparse
from pathlib import Path

from validate_package import LANGUAGES, TEXT_BLOCK_RE, is_active_png, sidecar_kinds_for
from validate_x_post_format import validate_file


def sync(package: Path, *, write: bool = False) -> list[Path]:
    pending: list[tuple[Path, str]] = []
    errors: list[str] = []
    # Validate all sources and resolve exactly one target per language before writing.
    for lang, word in LANGUAGES.items():
        source = package / f"x-post-{lang}.md"
        errors.extend(validate_file(source, "出典メモ：" if lang == "ja" else "Source note:", language=lang))
        targets = [p for p in (package / "images").glob(f"*_{word}_posting*.png") if is_active_png(p)]
        if len(targets) != 1:
            errors.append(f"{package}: expected one selected {word} posting PNG, found {len(targets)}")
            continue
        if source.is_file():
            blocks = TEXT_BLOCK_RE.findall(source.read_text(encoding="utf-8"))
            kinds = sidecar_kinds_for(package)
            if len(blocks) == len(kinds):
                pending.extend((targets[0].with_suffix(f".{kind}.txt"), block.strip() + "\n")
                               for kind, block in zip(kinds, blocks))
    if errors:
        raise ValueError("\n".join(errors))
    changed = []
    for path, content in pending:
        if path.is_file() and path.read_text(encoding="utf-8").strip() == content.strip():
            continue
        changed.append(path)
        if write:
            temp = path.with_suffix(path.suffix + ".sync-tmp")
            temp.write_text(content, encoding="utf-8", newline="\n")
            temp.replace(path)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("--write", action="store_true", help="write derived sidecars; otherwise check only")
    args = parser.parse_args()
    try:
        changed = sync(args.package.resolve(), write=args.write)
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}")
        return 1
    if changed and not args.write:
        print("ERROR: sidecars need synchronization:\n" + "\n".join(map(str, changed)))
        return 1
    print(f"OK: sidecars synchronized ({len(changed)} updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
