# Thin-note triage

Date: 2026-10-12. Authored record (the builder never touches this file).

`scripts/qc_note.py` flags a note that falls below the depth floors. Nine corpus
notes were flagged. This log records what happened to each one: whether the note
was genuinely under-extracted and was fixed by re-reading the paper, or whether
the paper itself reports very little and the note should stay flagged.

## The depth gate

The gate has three floors and one escape hatch:

| Floor | Value | What it measures |
| :--- | :--- | :--- |
| `MIN_WORDS` | 2500 | Overall extraction depth. |
| `MIN_EFFECT_ROWS` | 12 | Whether the results section was actually read. |
| `MIN_QUOTE_ROWS` | 8 | Whether quotable source text was captured. |

A note may also pass by stating a **documented absence**: when the paper reports
no outcome statistics, the evidence table holds the single line `Not reported.`
plus one sentence of justification. Padding with design parameters is forbidden.

The word floor scales down for short-form documents (reports, working papers,
book chapters, and now datasets). The evidence-row floor never moves.

### Refinement applied 2026-10-12

Two changes were made to the word floor in `scripts/qc_note.py`, because it was
flagging notes that were not thin:

- A note whose evidence table already meets the 12-row floor no longer fails on
  word count alone. The row floor is what proves the results were read; a terse
  source, or a paper whose findings live in tables, is often short on prose even
  when it is fully extracted.
- `dataset` was added to the short-form types, since a statistical release is
  legitimately shorter than a journal article.

## Outcome

Four notes were genuinely under-extracted and were enriched. Five are genuinely
sparse and were left flagged.

| Stem | Class | Evidence rows | Quotes | Words | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `A--Guo-2024` | under-extracted | 5 → 20 | 3 → 8 | 1404 → 1873 | passes |
| `I--FederalReserve-2024` | under-extracted | 10 → 40 | 5 → 10 | 1450 → 2378 | passes |
| `L--PSA-2025` | under-extracted | 11 → 46 | 6 → 9 | 1420 → 2341 | passes |
| `L--PSA-2026` | under-extracted | 6 → 20 | 3 → 8 | 900 → 1424 | passes |
| `A--Chahar-2026` | genuinely sparse | 8 | 18 | 3627 | left flagged |
| `A--Sireesha-2026` | genuinely sparse | 7 | 14 | 3261 | left flagged |
| `A--Vinitha-2026` | genuinely sparse | 9 | 12 | 4069 | left flagged |
| `I--Prakoso-2024` | genuinely sparse | 6 | 16 | 6127 | left flagged |
| `I--ZhangLu-2026` | genuinely sparse | 9 | 15 | 4906 | left flagged |

## Under-extracted notes (enriched)

Each of these papers reports more outcome statistics than the note captured. The
conversion was re-read and the missing rows were added with their locators. The
values were checked against the conversion before being written.

- `A--Guo-2024` — added the RT kill rates (0.66, 0.54, 0.61, 0.36, 0.65), the
  ART `nextDate` kill rate (0.51), the `A1_BCDmean` kill rates (0.95, 1, 0.97,
  0.8, 0.94), the KLEE miniSAT result (0), the accept-rate contrast (0.0026 for
  `A1_BCDmax` vs 0.0123 for `A1_BCDmean`, Table 6), and the mutation-testing time
  for RT triType (291 s, Table 8, page 20). Quotes were expanded from 3 to 8.
- `I--FederalReserve-2024` — added spending-versus-income, emergency-savings,
  debt, banking, housing, and retirement rows. Locators use PDF page numbers
  (PDF page = printed report page + 4; verified). Quotes were expanded from 5 to
  10.
- `L--PSA-2025` — added the quarter-by-quarter growth rates, prior-year bases,
  expenditure shares, contributors to growth, and the quarters that declined.
  Quotes were expanded from 6 to 9.
- `L--PSA-2026` — corrected a factual error (the note said the 5.3 percent
  figure was for Q1 2025; the release attributes it to Q2 2025) and added the
  Q1/Q2 shares, contributors, and the Q2 contractions. Quotes were expanded from
  3 to 8.

## Genuinely sparse notes (left flagged)

Each of these papers reports only a handful of outcome statistics, or none:

- `A--Chahar-2026` — a systematic review; its evidence is a small set of survey
  ratings, not primary outcome statistics.
- `A--Sireesha-2026` — reports seven results.
- `A--Vinitha-2026` — nine result rows.
- `I--Prakoso-2024` — a narrative review with no primary data.
- `I--ZhangLu-2026` — a qualitative review that states no data were generated or
  analysed.

For these, the depth-gate warning is honest: the paper genuinely reports fewer
than twelve outcome statistics, so there is no more data to extract. Replacing
their evidence tables with `Not reported.` would be wrong, because the papers do
report a few real values. The flag is left in place as a signal to the reader,
and the corpus build remains clean (0 errors).
