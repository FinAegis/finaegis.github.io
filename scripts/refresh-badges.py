#!/usr/bin/env python3
"""Refresh live badges in index.html by querying the GitHub REST API.

Replaces the text content of any element carrying a `data-live` attribute
whose value matches a known key. Currently handles star counts.

Run locally with `gh` authenticated, or via the refresh-badges workflow.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPOS = [
    "core-banking-prototype-laravel",
    "defluff",
    "cli",
    "php-sdk",
    "payment-sdk",
]

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX = REPO_ROOT / "index.html"


def gh_api(path: str) -> dict:
    out = subprocess.run(
        ["gh", "api", path],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return json.loads(out)


def fetch_stars() -> dict[str, int]:
    return {name: int(gh_api(f"repos/FinAegis/{name}")["stargazers_count"]) for name in REPOS}


def replace_live(html: str, key: str, value: str) -> tuple[str, int]:
    pattern = re.compile(rf'(data-live="{re.escape(key)}"[^>]*>)([^<]*)(</)')
    hits = 0

    def sub(match: re.Match) -> str:
        nonlocal hits
        hits += 1
        return match.group(1) + value + match.group(3)

    return pattern.sub(sub, html), hits


def main() -> int:
    if not INDEX.exists():
        print(f"error: {INDEX} not found", file=sys.stderr)
        return 1

    src = INDEX.read_text()
    stars = fetch_stars()
    total = sum(stars.values())

    src, hits = replace_live(src, "stars-total", str(total))
    if hits == 0:
        print("warn: no data-live='stars-total' element found", file=sys.stderr)

    for name, count in stars.items():
        src, _ = replace_live(src, f"stars-{name}", str(count))

    INDEX.write_text(src)

    print(f"total={total}")
    for name, count in stars.items():
        print(f"  {name}={count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
