#!/usr/bin/env python3
"""Build index.html from factory-protocol.html (README.md, DECISION-002).

index.html is factory-protocol.html inside a document wrapper. Edit the
source page, then run: python3 scripts/build_index.py
tests/test_page.py fails if index.html is not what this script writes.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "factory-protocol.html"
TARGET = ROOT / "index.html"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
</head>
<body>
"""
TAIL = """
</body>
</html>
"""


def build(fragment: str) -> str:
    """The full document for a page fragment."""
    return HEAD + fragment + TAIL


def main() -> None:
    TARGET.write_text(build(SOURCE.read_text(encoding="utf-8")), encoding="utf-8")


if __name__ == "__main__":
    main()
