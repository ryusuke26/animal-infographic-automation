"""Offline adapter to the pinned official twitter-text JavaScript parser."""

from functools import lru_cache
import json
import os
from pathlib import Path
import shutil
import subprocess


@lru_cache(maxsize=128)
def count_post(text: str) -> tuple[int, bool]:
    node = os.environ.get("INFOGRAPHIC_NODE") or shutil.which("node")
    if not node:
        raise ValueError("X counting needs Node.js; set INFOGRAPHIC_NODE to its executable")
    helper = Path(__file__).parent / "x-text" / "count.cjs"
    try:
        result = subprocess.run(
            [node, str(helper)], input=json.dumps([text]), text=True,
            encoding="utf-8", capture_output=True, timeout=20,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ValueError(f"X character counter could not run: {exc}") from exc
    if result.returncode:
        raise ValueError(
            "X character counter failed; install the pinned local dependency once "
            "with npm ci --prefix scripts/x-text --ignore-scripts --no-audit --no-fund"
        )
    try:
        value = json.loads(result.stdout)[0]
        return int(value["weightedLength"]), bool(value["valid"])
    except (ValueError, KeyError, IndexError, TypeError) as exc:
        raise ValueError("X character counter returned an invalid result") from exc
