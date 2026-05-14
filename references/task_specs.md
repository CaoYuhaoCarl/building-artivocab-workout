# Task Specs — reading-vocab-cloze

Detailed rules for each task. Read this before executing any of Step 0 / Task 1–7.

## Baseline Text

- **Source article**: the user-provided article before any simplification.
- **Worksheet article**: the Step 0 output. If adaptation is skipped, the worksheet article is the unchanged source article.
- Build Tasks 1–7 from the worksheet article so the vocabulary list, cloze blanks, and answer highlights stay aligned.

## Step 0: B1 Adaptation

Normalize to upper-A2/B1 unless the user asks to keep the original wording.

- Keep all facts, timeline, and logic unchanged.
- Replace niche, technical, or Latinate words with plain high-frequency equivalents.
- Keep specialist terms that are essential to the article's meaning; simplify the surrounding sentence instead.
- Preserve natural register — do not make it sound like a textbook.
- **Stopping criterion:** If the passage has no C1+ vocabulary and sentences average 15–22 words, skip adaptation and note "Source passage retained without adaptation."

**Typical simplification swaps:**
- `rejuvenating` → `make people feel fresh again`
- `traumatic chapters` → `painful periods`
- `endured` → `lived through` / `survived`
- `indomitability` → `strength` / `refusal to give up`
- `mirrors the determination` → `shows the determination`

## Task 1: 20 core words

- Exclude proper nouns (people, countries, dates, publication names).
- Keep difficulty at B1 or below.
- Prefer words that affect comprehension of policy, action, cause/effect, attitude, and consequence.
- Prefer one headword per word family. Use the base form when it is the clearer teaching anchor; use the article form when the derived meaning is the actual comprehension target.
- Put the article-used surface form into `派生词:` when the headword is normalized away from it.
- Add `派生词:` for morphology-rich words with clear classroom transfer (verb/noun/adjective/adverb shifts, common confusables). Keep to 1–3 high-value family members. Skip when the family is trivial or unhelpful.
- Strictly follow `assets/group_format_template.md` for layout.

### Task 1 ordering

Use the controlled-shuffle algorithm — do not list words in article order:

1. Group words by part of speech: verbs / nouns / adjectives+adverbs / other.
2. Sort within each group by first appearance in the article.
3. Output in round-robin: one verb, one noun, one adjective/adverb, repeat; skip exhausted groups.

Use article-order only if the user explicitly requests it.

## Task 2: full-group masking

Mask every Task 1 target in the worksheet article with `==word==`, using the actual surface form in the passage (not the headword). Preserve all paragraphing and punctuation.

## Task 3: 10 assessment words

Select 10 words from Task 1.

**Distribution constraints:**
- One word per sentence. Sentence boundary: ends at `.` `?` `!`; semicolon clauses and direct-quotation+attribution count as one sentence.
- Spread evenly across the worksheet article; avoid clustering at the start or end.

**Assessment balance** (aim for this; adjust when the article doesn't support it):
- 3 semantic — core meaning words carrying cause/effect, attitude, or consequence
- 3 grammar-sensitive — form matters for syntax, tense, voice, or inflection
- 2 collocation — tied to fixed or semi-fixed expressions in context
- 2 transferable high-frequency — strong reuse value in future reading/writing/speaking

For morphology-rich entries, prefer testing via word formation over direct surface-form recall.

## Task 4: numbered cloze blanks

Replace each of the 10 Task 3 words exactly once in the worksheet article with `` `1________` ``, `` `2________` `` … using **exactly 8 underscores**. Number in reading order. Preserve all other wording and paragraph breaks.

**Word-formation integration:** When 2–4 items are tested via word formation, add a **Cue list** immediately after the article block (before Task 5):
```
Blank N → [cue form]
```
The cue is a related family member; the learner must supply the article-correct form. Omit the cue list entirely if no word-formation blanks are used.

**Worked example — direct recall vs word-formation blank:**

```
The factory `1________` more than 500 workers last year. Despite rising costs,
the company continued to `2________` [expand] its operations overseas.
```

- Blank 1 — direct surface recall (no cue).
- Blank 2 — word-formation: cue `[expand]`, expected answer is whatever form the sentence demands (e.g. `expanding` or `expanded`). Cue and answer must belong to the same family.

## Task 5: final 10-word highlighting

Return to the unmasked worksheet article. Mark only the 10 Task 3 answers with `==word==`. Do not carry over Task 2 masking or highlight the full Task 1 set.

## Task 6: Output Activation

Add four short classroom prompts after Task 5:

- **6A – 3-word retelling:** Retell the news in 2–3 sentences using at least 3 target words.
- **6B – 5-sentence summary:** Summarize the event in exactly 5 sentences.
- **6C – Cause-effect chain:** Explain the event using *because / therefore / as a result*.
- **6D – Perspective response:** Respond from a role in the article. Tailor the role to the article's topic. Examples: *"If you were a European buyer, what would worry you most?"* / *"If you were an energy analyst, what would you watch next?"* / *"If you were the policymaker, what would you prioritize first?"* Keep prompts short, clear, and ready for direct classroom use.

## Task 7: Advanced Training

Add two sub-sections after Task 6.

#### 写作-高阶训练

Select 3 sentences from the worksheet article that contain target vocabulary or grammatically rich structures. For each, provide:
- A blank line for the student to write the English sentence
- The Chinese translation of that sentence directly below
- Keep key vocabulary hints in parentheses (e.g. `all-round`) where they help without giving the answer away

Format:
```
`________________________________________________________________`
[Chinese translation of the sentence，key hint in parentheses if useful]
```

#### 阅读-高阶训练

Select 1 challenging word, phrase, or term from the worksheet article — preferably one that is inferrable from surrounding context. Ask the student to guess its meaning from context.

Format:
```
通过上下文语境，猜测[paragraph reference]中"[term]"的含义
`________________________________________________________________`
```

## Pre-delivery checks

Only the non-obvious ones that are easy to drift on:

- Task 4 has exactly 10 numbered blanks, in reading order.
- No sentence has more than one Task 3 word.
- Task 5 highlights the same 10 answers as Task 3 — not the Task 2 set.
- Tasks 2, 4, and 5 all use the same worksheet article baseline.
- If word-formation cues are used, the expected answer matches the article sentence exactly.
- Task 1 morphology coverage is moderate: not zero, not every entry.
