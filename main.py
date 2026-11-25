"""Fridge Roast: one locked line, delivered to /output/entry.txt."""

import sys
from pathlib import Path

ENTRY = "I opened the fridge for a snack and it just stood there, humming, with one sad pickle and a jar of something that expired during the Obama administration."
LIMIT = 200
EXPECTED_CHARS = 154


def check(line: str, limit: int) -> None:
    if not line:
        raise SystemExit("empty entry")
    if line != line.strip():
        raise SystemExit("entry has surrounding whitespace")
    if any(ch in line for ch in "\n\r"):
        raise SystemExit("entry must be a single line")
    size = len(line.encode("utf-8"))
    if size > limit:
        raise SystemExit(f"entry is {size} bytes, over the {limit} limit")


def main() -> int:
    if len(ENTRY) != EXPECTED_CHARS:
        raise SystemExit(f"entry changed: {len(ENTRY)} chars, expected {EXPECTED_CHARS}")
    check(ENTRY, LIMIT)
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")
    if target.read_text(encoding="utf-8") != ENTRY:
        raise SystemExit("round-trip mismatch")
    print(f"entry written: {len(ENTRY)} chars -> {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
