---
name: reading-vocab-cloze
description: "Build Chinese-English reading cloze worksheets from a reading passage or a markdown file. TRIGGER when: user pastes an article or news text and asks for vocabulary extraction, cloze blanks, or a reading worksheet; user says '做完形填空'、'出词汇题'、'帮我做阅读练习题'、'生成词汇表' or similar Chinese EFL requests; user provides a markdown file following the Day_test layout and wants it completed. Produces: B1-adapted passage, 20-word Group block (Task 1), full-masking article (Task 2), 10-word assessment list (Task 3), numbered cloze article (Task 4), answer-key highlighted article (Task 5), classroom output-activation prompts (Task 6), and advanced writing+reading training (Task 7)."
---

# reading-vocab-cloze

Goal: a completed Day_test-style worksheet that tests meaning, grammar sensitivity, collocation, morphology, and output transfer — not just blank recognition.

## Core Terms

- **Source article** — the text provided by the user.
- **Worksheet article** — the Step 0 result: either the B1-adapted article or the unchanged source article when adaptation is skipped.
- Use the worksheet article for Tasks 1–7. In Task 5, "original article" means the unmasked worksheet article, not the pre-adaptation source.

## Workflow

Before executing any task, **read `references/task_specs.md`** — the rules live there. Steps below are action labels only.

1. Read the source markdown; identify article body and task slots.
2. Run **Step 0** (B1 adaptation).
3. Read `assets/group_format_template.md`.
4. **Task 1** — 20-word group block.
   - Run `scripts/validate_group_block.py` on the prepared Task 1 block before final delivery.
5. **Task 2** — full-group masking in article.
6. **Task 3** — pick 10 assessment words.
7. **Task 4** — numbered cloze blanks (+ Cue list if word-formation used).
8. **Task 5** — highlight only the 10 Task 3 answers in the unmasked worksheet article.
9. **Task 6** — output activation prompts (6A–6D).
10. **Task 7** — advanced training (writing + reading).
11. Run **Pre-delivery checks** from task_specs.md.
    - For scriptable checks, create a temporary answer list containing the 10 Task 3 expected surface forms, then run `scripts/validate_final_output.py`.
12. Save to `output_dir` using the `filename format` defined in `assets/config.md`, unless the user requests otherwise.

## Decision points

- **Skip adaptation?** Yes if the source has no C1+ vocab and sentences average 15–22 words. Note "Source passage retained without adaptation."
- **Article-order vs controlled-shuffle for Task 1?** Default to controlled-shuffle. Use article-order only if the user explicitly asks.
- **Cue list in Task 4?** Include only when 2–4 blanks are tested via word formation; otherwise omit entirely.
- **`派生词:` coverage in Task 1?** Moderate — not zero, not every entry. Skip when the word family is trivial.

## Resources

- `references/task_specs.md` — **detailed rules for Step 0 and Task 1–7, plus pre-delivery checks. Read before executing any task.**
- `assets/config.md` — output_dir and other parameterized values.
- `assets/day_test_template_v2.md` — blank worksheet template.
- `assets/group_format_template.md` — required formatting reference for Task 1.
- `scripts/build_output.py` — assemble final markdown from the worksheet article and prepared Task 1–7 outputs.
- `scripts/validate_group_block.py` — validate Task 1 entry count, derived-word coverage, and line length.
- `scripts/validate_final_output.py` — validate Task 4 blank numbering/count, one blank per sentence, and Task 5 answer highlighting against a 10-line answer file.
