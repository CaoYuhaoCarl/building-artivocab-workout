# Config — reading-vocab-cloze

## output_dir

`/Users/carl/Desktop/openclaw/english_coach/reading_cloze`

Default save location for completed worksheets. Used in Workflow step 12.

Override only when the user explicitly:
- asks to overwrite an existing file (save in-place at the source path), or
- specifies a different absolute or relative path in the request.

## filename format

`YYYY_MM_DD_article_name.md`

Rules:
- **Date** — use the article's publication date when present in the source. If absent, fall back to today's date. Always zero-pad month and day (`2026_05_03`, not `2026_5_3`).
- **article_name** — short slug derived from the article headline:
  - lowercase
  - English words only; transliterate or translate Chinese headlines to a short English slug
  - words joined with single underscores `_`
  - strip articles (`a`, `an`, `the`), punctuation, and emoji
  - cap at 6 words / 60 characters; trim trailing words rather than mid-word
- **Extension** — always `.md`.

Examples:
- `2026_05_03_japan_minimum_wage_hike.md`
- `2026_04_19_shanghai_auto_show_ev_lineup.md`
- `2026_03_28_openai_gpt_pricing_cut.md`

Collision handling: if the target filename already exists in `output_dir`, append `_v2`, `_v3`, … before the extension. Do not overwrite unless the user explicitly asks.
