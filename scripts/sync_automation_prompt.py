#!/usr/bin/env python3
"""Safely synchronize a canonical prompt file into one local Automation TOML."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import time
import tomllib
from pathlib import Path


MUTABLE_KEYS = {"prompt", "updated_at"}


def parse_toml_text(text: str) -> dict:
    return tomllib.loads(text)


def build_candidate(original: str, prompt: str, updated_at: int) -> str:
    prompt_literal = json.dumps(prompt, ensure_ascii=False)
    candidate, prompt_count = re.subn(
        r"^prompt = .*$",
        lambda _: f"prompt = {prompt_literal}",
        original,
        count=1,
        flags=re.MULTILINE,
    )
    candidate, updated_count = re.subn(
        r"^updated_at = \d+$",
        lambda _: f"updated_at = {updated_at}",
        candidate,
        count=1,
        flags=re.MULTILINE,
    )
    if prompt_count != 1 or updated_count != 1:
        raise ValueError(
            "expected exactly one prompt field and one updated_at field "
            f"(found prompt={prompt_count}, updated_at={updated_count})"
        )
    return candidate


def verify_transition(before: dict, after: dict, expected_prompt: str, expected_id: str) -> None:
    if before.get("id") != expected_id or after.get("id") != expected_id:
        raise ValueError(f"unexpected automation id; expected {expected_id!r}")
    if after.get("prompt") != expected_prompt:
        raise ValueError("parsed TOML prompt does not exactly match canonical prompt file")
    if not isinstance(after.get("updated_at"), int):
        raise ValueError("updated_at is not an integer")

    for key, value in before.items():
        if key not in MUTABLE_KEYS and after.get(key) != value:
            raise ValueError(f"protected Automation field changed: {key}")

    extra_keys = set(after) - set(before)
    if extra_keys:
        raise ValueError(f"unexpected Automation fields added: {sorted(extra_keys)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--automation-toml", required=True, type=Path)
    parser.add_argument("--prompt-file", required=True, type=Path)
    parser.add_argument("--expected-id", default="automation-2")
    parser.add_argument("--backup", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    automation_toml = args.automation_toml.resolve()
    prompt_file = args.prompt_file.resolve()
    original = automation_toml.read_text(encoding="utf-8")
    prompt = prompt_file.read_text(encoding="utf-8")
    before = parse_toml_text(original)

    if args.check:
        if before.get("id") != args.expected_id:
            raise ValueError(f"unexpected automation id: {before.get('id')!r}")
        if before.get("prompt") != prompt:
            raise ValueError("live Automation prompt is not synchronized")
        print(
            json.dumps(
                {
                    "id": before["id"],
                    "status": before.get("status"),
                    "rrule": before.get("rrule"),
                    "model": before.get("model"),
                    "execution_environment": before.get("execution_environment"),
                    "prompt_chars": len(prompt),
                    "updated_at": before.get("updated_at"),
                },
                ensure_ascii=False,
            )
        )
        return 0

    candidate = build_candidate(original, prompt, int(time.time() * 1000))
    after = parse_toml_text(candidate)
    verify_transition(before, after, prompt, args.expected_id)

    backup = args.backup.resolve() if args.backup else automation_toml.with_suffix(".toml.bak")
    if not backup.exists():
        shutil.copy2(automation_toml, backup)

    temp = automation_toml.with_name(f".{automation_toml.name}.codex-sync.tmp")
    temp.write_text(candidate, encoding="utf-8", newline="")
    parsed_temp = parse_toml_text(temp.read_text(encoding="utf-8"))
    verify_transition(before, parsed_temp, prompt, args.expected_id)
    os.replace(temp, automation_toml)

    final = parse_toml_text(automation_toml.read_text(encoding="utf-8"))
    verify_transition(before, final, prompt, args.expected_id)
    print(
        json.dumps(
            {
                "id": final["id"],
                "status": final.get("status"),
                "rrule": final.get("rrule"),
                "model": final.get("model"),
                "execution_environment": final.get("execution_environment"),
                "target": final.get("target"),
                "cwds": final.get("cwds"),
                "prompt_chars": len(prompt),
                "updated_at": final.get("updated_at"),
                "backup": str(backup),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
