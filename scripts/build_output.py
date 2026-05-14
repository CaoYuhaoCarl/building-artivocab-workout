#!/usr/bin/env python3
import argparse
from pathlib import Path

TASK1 = "[Task 1输出结果处]"
TASK2 = "[Task 2输出结果处]"
TASK3 = "[Task 3输出结果处]"
TASK4 = "[Task 4输出结果处]"
TASK5 = "[Task 5输出结果处]"
TASK6 = "[Task 6输出结果处]"
TASK7 = "[Task 7输出结果处]"
ARTICLE = "[在这里粘贴原文]"


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise ValueError(f"Placeholder not found: {old}")
    return text.replace(old, new, 1)


def main():
    p = argparse.ArgumentParser(description="Fill the reading cloze markdown template with prepared results.")
    p.add_argument("--template", required=True, help="Path to the template markdown file")
    p.add_argument("--article", required=True, help="Path to a plain text/markdown file containing the worksheet article")
    p.add_argument("--group", required=True, help="Path to text file containing Task 1 output")
    p.add_argument("--task2", required=True, help="Path to text file containing Task 2 output")
    p.add_argument("--task3", required=True, help="Path to text file containing Task 3 output")
    p.add_argument("--task4", required=True, help="Path to text file containing Task 4 output")
    p.add_argument("--task5", required=True, help="Path to text file containing Task 5 output")
    p.add_argument("--task6", required=True, help="Path to text file containing Task 6 output")
    p.add_argument("--task7", required=True, help="Path to text file containing Task 7 output")
    p.add_argument("--output", required=True, help="Output markdown path")
    args = p.parse_args()

    template = Path(args.template).read_text(encoding="utf-8")
    article = Path(args.article).read_text(encoding="utf-8").strip()
    group = Path(args.group).read_text(encoding="utf-8").strip()
    task2 = Path(args.task2).read_text(encoding="utf-8").strip()
    task3 = Path(args.task3).read_text(encoding="utf-8").strip()
    task4 = Path(args.task4).read_text(encoding="utf-8").strip()
    task5 = Path(args.task5).read_text(encoding="utf-8").strip()
    task6 = Path(args.task6).read_text(encoding="utf-8").strip()
    task7 = Path(args.task7).read_text(encoding="utf-8").strip()

    output = replace_once(template, ARTICLE, article)
    output = replace_once(output, TASK1, TASK1 + "\n\n" + group)
    output = replace_once(output, TASK2, TASK2 + "\n\n" + task2)
    output = replace_once(output, TASK3, TASK3 + "\n\n" + task3)
    output = replace_once(output, TASK4, TASK4 + "\n\n" + task4)
    output = replace_once(output, TASK5, TASK5 + "\n\n" + task5)
    output = replace_once(output, TASK6, TASK6 + "\n\n" + task6)
    output = replace_once(output, TASK7, TASK7 + "\n\n" + task7)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output, encoding="utf-8")
    print(output_path)


if __name__ == "__main__":
    main()
