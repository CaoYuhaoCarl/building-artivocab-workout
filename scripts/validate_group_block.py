#!/usr/bin/env python3
"""Validate a prepared Task 1 Group block for the reading-vocab-cloze skill."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ENTRY_RE = re.compile(r"^\*\*(.+?)\*\*\s*/", re.MULTILINE)
DERIVED_PREFIX = "派生词:"
SEPARATOR = "──────────────────────────────"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a Task 1 Group block and warn about derived-word coverage."
    )
    parser.add_argument("path", help="Path to a prepared Task 1 Group block text file")
    parser.add_argument("--expected-count", type=int, default=20, help="Expected number of entries (default: 20)")
    parser.add_argument(
        "--min-derived-coverage",
        dest="min_derived_coverage",
        type=float,
        default=0.25,
        help="Warn if derived-word coverage falls below this ratio (default: 0.25)",
    )
    parser.add_argument(
        "--max-derived-coverage",
        dest="max_derived_coverage",
        type=float,
        default=0.75,
        help="Warn if derived-word coverage exceeds this ratio (default: 0.75)",
    )
    parser.add_argument(
        "--max-derived-line-length",
        dest="max_derived_line_length",
        type=int,
        default=60,
        help="Warn if a 派生词 line exceeds this many characters (default: 60)",
    )
    return parser.parse_args()


def split_entries(text: str) -> list[str]:
    parts = [part.strip() for part in text.split(SEPARATOR)]
    return [part for part in parts if ENTRY_RE.search(part)]


def find_headword(entry: str) -> str:
    match = ENTRY_RE.search(entry)
    return match.group(1).strip() if match else "<unknown>"


def main() -> int:
    args = parse_args()
    text = Path(args.path).read_text(encoding="utf-8")
    entries = split_entries(text)

    entry_count = len(entries)
    derived_entries: list[str] = []
    missing_entries: list[str] = []
    long_lines: list[tuple[str, int, str]] = []

    for entry in entries:
        headword = find_headword(entry)
        derived_line = next((line.strip() for line in entry.splitlines() if line.strip().startswith(DERIVED_PREFIX)), None)
        if derived_line:
            derived_entries.append(headword)
            if len(derived_line) > args.max_derived_line_length:
                long_lines.append((headword, len(derived_line), derived_line))
        else:
            missing_entries.append(headword)

    coverage = (len(derived_entries) / entry_count) if entry_count else 0.0

    print(f"FILE: {args.path}")
    print(f"ENTRY_COUNT: {entry_count}")
    print(f"EXPECTED_COUNT: {args.expected_count}")
    print(f"DERIVED_LINES: {len(derived_entries)}")
    print(f"DERIVED_COVERAGE: {coverage:.0%}")
    print()

    issues: list[str] = []

    if entry_count != args.expected_count:
        issues.append(f"WARN entry count mismatch: expected {args.expected_count}, found {entry_count}")
    else:
        issues.append(f"OK entry count matches expected {args.expected_count}")

    if coverage < args.min_derived_coverage:
        issues.append(
            f"WARN derived coverage looks low: {coverage:.0%} < {args.min_derived_coverage:.0%}"
        )
    elif coverage > args.max_derived_coverage:
        issues.append(
            f"WARN derived coverage looks high: {coverage:.0%} > {args.max_derived_coverage:.0%}"
        )
    else:
        issues.append(
            f"OK derived coverage is within range {args.min_derived_coverage:.0%}–{args.max_derived_coverage:.0%}"
        )

    if derived_entries:
        issues.append("INFO entries with 派生词: " + ", ".join(derived_entries))
    else:
        issues.append("WARN no 派生词 lines found")

    if missing_entries:
        issues.append("INFO entries without 派生词: " + ", ".join(missing_entries))

    if long_lines:
        for headword, length, line in long_lines:
            issues.append(
                f"WARN 派生词 line too long for {headword} ({length} chars): {line}"
            )
    else:
        issues.append(
            f"OK no 派生词 line exceeds {args.max_derived_line_length} characters"
        )

    for issue in issues:
        print(issue)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
