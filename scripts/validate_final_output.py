#!/usr/bin/env python3
"""Validate final Task 4/Task 5 consistency for building-artivocab-workout outputs."""

from __future__ import annotations

import argparse
import re
import unicodedata
from collections import Counter
from pathlib import Path

BLANK_RE = re.compile(r"`([1-9]|10)_{8}`")
ANY_BACKTICK_BLANK_RE = re.compile(r"`\d+_+`")
HIGHLIGHT_RE = re.compile(r"==([^=\n]+)==")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate Task 4 blank numbering and Task 5 highlighted answers."
    )
    parser.add_argument("--task4", required=True, help="Path to prepared Task 4 output")
    parser.add_argument("--task5", required=True, help="Path to prepared Task 5 output")
    parser.add_argument(
        "--answers",
        required=True,
        help="Path to a 10-line file containing expected Task 3 answer surface forms",
    )
    parser.add_argument("--expected-count", type=int, default=10, help="Expected answer count")
    return parser.parse_args()


def normalize_answer(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = value.strip().strip("`*= ")
    value = re.sub(r"^\s*(?:[-*]|\d+[.)-])\s*", "", value)
    value = value.strip().strip("`*= ")
    value = re.sub(r"\s+", " ", value)
    return value.casefold()


def read_answers(path: Path) -> list[str]:
    answers: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        answer = normalize_answer(line)
        if answer:
            answers.append(answer)
    return answers


def find_sentence_blank_issues(task4: str) -> list[str]:
    issues: list[str] = []
    sentences = re.split(r"(?<=[.!?])\s+", task4)
    for index, sentence in enumerate(sentences, start=1):
        blanks = BLANK_RE.findall(sentence)
        if len(blanks) > 1:
            issues.append(
                f"Task 4 sentence {index} contains more than one blank: {', '.join(blanks)}"
            )
    return issues


def main() -> int:
    args = parse_args()
    task4 = Path(args.task4).read_text(encoding="utf-8")
    task5 = Path(args.task5).read_text(encoding="utf-8")
    answers = read_answers(Path(args.answers))

    issues: list[str] = []

    malformed_blanks = ANY_BACKTICK_BLANK_RE.findall(task4)
    exact_blanks = BLANK_RE.findall(task4)
    if len(malformed_blanks) != len(exact_blanks):
        issues.append("Task 4 contains malformed blank markers; use `N________` with exactly 8 underscores.")

    blank_numbers = [int(number) for number in exact_blanks]
    expected_numbers = list(range(1, args.expected_count + 1))
    if blank_numbers != expected_numbers:
        issues.append(f"Task 4 blank numbers should be {expected_numbers}, found {blank_numbers}.")

    issues.extend(find_sentence_blank_issues(task4))

    if len(answers) != args.expected_count:
        issues.append(f"Answer file should contain {args.expected_count} answers, found {len(answers)}.")

    highlighted = [normalize_answer(match) for match in HIGHLIGHT_RE.findall(task5)]
    if len(highlighted) != args.expected_count:
        issues.append(f"Task 5 should highlight {args.expected_count} answers, found {len(highlighted)}.")

    if ANY_BACKTICK_BLANK_RE.search(task5):
        issues.append("Task 5 should be an answer-key highlight article, not a numbered cloze article.")

    expected_counter = Counter(answers)
    highlighted_counter = Counter(highlighted)
    if expected_counter != highlighted_counter:
        missing = sorted((expected_counter - highlighted_counter).elements())
        extra = sorted((highlighted_counter - expected_counter).elements())
        if missing:
            issues.append("Task 5 is missing highlighted answer(s): " + ", ".join(missing))
        if extra:
            issues.append("Task 5 has unexpected highlighted answer(s): " + ", ".join(extra))

    print(f"TASK4_BLANKS: {len(exact_blanks)}")
    print(f"TASK5_HIGHLIGHTS: {len(highlighted)}")
    print(f"ANSWERS: {len(answers)}")

    if issues:
        print("RESULT: FAIL")
        for issue in issues:
            print("FAIL " + issue)
        return 1

    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
