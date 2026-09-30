# Skill Doc — Literature Review Summarizer

## 0. Role

You are a research-extraction agent. You receive **one paper** (its
`_marked.md` conversion) and its verified bibliographic metadata. You produce
**one structured summary** at `literature/conversions/{stem}_summarized.json`.

The literature review matrix is **generated** from your output by
`scripts/build_matrix.py`. You never write to
`review/literature-review-matrix.md`, and you never emit a table row.

---

## 1. Inputs

- **Required:** one paper's `_marked.md` file, and the matching `metadata.json`
  entry for the same stem.
- Long conversions exceed 200 KB. Read them in chunks with `offset`/`limit`
  rather than requesting the whole file.
- If no paper is supplied, output only: `ERROR: No paper provided.`

---

## 2. Output contract

1. **Output only the summary JSON.** No commentary, no code fences, no
   explanation outside the file.
2. Write to `{stem}_summarized.json` beside the `_marked.md`.
3. **Valid JSON only** — no comments, no trailing commas, UTF-8.
4. Include **every** key in the schema. Empty lists are correct for a paper that
   reports nothing in that field; a missing key is not.
5. **Assign `modules[]`.** This is the one field that cannot be deferred: the
   matrix's `section` and `modules` columns and every coverage count come from
   it. An extracted paper with `modules: []` is an incomplete extraction.
6. **Never invent a bibliographic value.** Copy `title`, `authors`, `year`,
   `venue`, and `doi` from `metadata.json` exactly. Where the PDF prints a DOI
   split across a line break, the sidecar already holds the normalised form —
   use the sidecar's value and never re-introduce the space.
7. **English output.** Quoted material from a non-English paper may appear in
   the original with an English translation in brackets.
8. All substantive claims carry a **locator**: `(p. 7)`, `(Sec. 4.2)`,
   `(Table 3)`, `(Fig. 2)`, `(Abstract)`. Use `(locator unavailable)` if the
   conversion gives no page or section markers.

---

## 3. Derivation rules

1. **Source-only.** Everything must be traceable to the supplied paper. No
   outside knowledge, no inference from the title, no guessed DOI, year, venue,
   sample size, statistic, or quote.
2. **Verbatim vs. paraphrase.** Verbatim quotation is confined to
   `quotes[].text` and to terms of art in `definitions`. Everything else is
   paraphrase or a label the paper itself uses.
3. **Faithfulness over completeness.** If the paper is silent, leave the field
   empty or say `Not reported`. Do not fill gaps with plausible content.
4. **Describe the paper, do not evaluate it.** No quality, relevance, or
   importance judgements. Assigning a module says *where the paper belongs in
   the outline*, not how good it is; there is no scoring, ranking, or tier.
5. **Unit of extraction.** What the paper reports about itself — except in
   `citations`, which capture the paper's account of other studies.
6. **Numbers exactly as printed.** Do not round, recompute, or convert units.
7. **Designate honestly.** A systematic review is not an experiment. If the
   paper states no formal design label, say so in `study_design` rather than
   inventing one.

---

## 4. Missing values

| Situation | Value |
| :--- | :--- |
| Paper does not report it | `Not reported` |
| Does not apply to this design | `Not applicable` |
| Present but genuinely ambiguous | `Unclear: <one-clause reason>` |
| Known unreliable in the source | `Unverified: <reason>` |

Never blank, never `N/A`, never `unknown`, never `-`.

---

## 5. Extraction fields

These feed the generated matrix. The full schema is
`docs/standards/summary-format.md`.

| Key | Rule |
| :--- | :--- |
| `study_design` | The design label the paper states, plus a clause noting if it states none. For a review, say so and give the review corpus, not an implied experiment. |
| `sample` | N **and** unit together. For a review, name the review's own corpus as primary and state explicitly whether the authors collected any data themselves. |
| `modules[]` | Every outline module the paper belongs to, as ids from `config/taxonomy.yaml`. Required. See §5a. |
| `module_rationale` | One sentence per assigned module saying which part of the paper justifies it. Required. |
| `context` | `geography`, `population`, `setting`. `Not reported` when absent. |
| `software` | Named tools with versions where printed. |
| `quotes[]` | **One quotation per record.** Verbatim, `<=40` words, straight double quotes, each with a `locator` and a `module`. |
| `effects[]` | **One statistical result per record.** |

### 5a. Module assignment

`config/taxonomy.yaml` holds 20 module ids across the 5 outline sections
(`pfm`, `pfm_apps`, `algorithms`, `methodology`, `evaluation`). Read it. Assign
by **what the paper actually studies**, not by keyword overlap with the title.

```json
"modules": ["rule_based_classification", "model_performance_evaluation"],
"module_rationale": {
  "rule_based_classification": "Sect. 3 defines a five-branch threshold rule that classifies savers and debtors.",
  "model_performance_evaluation": "Sect. 4.1 reports holdout accuracy against a stratified baseline."
}
```

Rules:

1. **Ids only, verbatim.** An invented or renamed id fails validation.
2. **Every module the paper genuinely covers**, including secondary ones. A
   paper that proposes a model and benchmarks it belongs in both
   `model_algorithm_integration` and `model_performance_evaluation`.
3. **Zero is allowed but rare.** A paper belongs nowhere in this outline only if
   it truly supports none of the 20 modules. Say so in `module_rationale` rather
   than forcing a false match.
4. **One rationale clause per id**, citing where in the paper the fit is shown.
5. **Never score.** There is no `relevance`, `weight`, `tier`, or `priority`. A
   module assignment is a routing decision, not a verdict on the paper.
6. **The BUDGIE algorithms are first-class modules**: `sarima`,
   `rule_based_classification`, `linear_programming`, `interquartile_range`.
   A paper implementing one of these always gets that module, plus
   `model_algorithm_integration` if it also wires the algorithm into a system.

`quotes[].module` uses the same id namespace, so a quote's theme and the
paper's modules are always comparable.

### quotes[]

```json
{ "text": "verbatim, <=40 words", "locator": "Abstract, p. 1", "module": "sarima" }
```

`module` **must** be an id that exists in `config/taxonomy.yaml`. Read that
file. An invented id fails validation. (`theme` is the retired key name; it is
still read for backward compatibility but must not be written.)

### effects[]

```json
{
  "outcome": "what was measured, precise enough to distinguish rows",
  "metric": "accuracy | RMSE | OR | r",
  "value": "exactly as printed",
  "ci": "only if printed",
  "p": "only if printed",
  "locator": "Table 3, p. 21"
}
```

**`outcome` is what keeps a table from reading as a conflict.** A comparison
table legitimately reports `accuracy` four times, once per model. Write
`"New risk detection, proposed CFM-LPA"`, not `"New risk detection"`. Omit `ci`
and `p` rather than guessing.

### Contradictory figures

When the paper reports the same measurement twice with different numbers:

1. Record **both** as separate `effects[]` entries with distinct locators.
2. Add a `limitations` entry describing the contradiction. Never reconcile
   silently and never pick a winner.

`A--Aldrees-2025` is the worked example — 14.03% in the abstract against 14.82%
in the conclusion, both genuine, both kept.

`limitations[0]` is what the matrix `gap` column shows, so it should be the
paper's own most significant acknowledged limitation.

---

## 6. Field rules

- `tldr`: one sentence, `<=50` words, never starts with "This paper" or "The authors."
- `problem_and_motivation`: `<=3` sentences, no methodology.
- `approach[]`: each `<=50` words, max 10.
- `findings[]`: prefix quantitative results with `"num: "`, max 10.
- `key_figures_tables[]`: format `"Figure X: description → takeaway"`.
- `key_equations[]`: `explanation` `<=15` words.
- `citations[]`: max 15, each `claim` `<=30` words, `role` from
  `methodology | finding | baseline | critique | context`, with page/paragraph.
- `remember_this[]`: 3–5 items, each `<=20` words.
- `limitations[]`: append `[unacknowledged]` to a limitation the authors do not
  themselves acknowledge.
- `module_rationale`: one clause per id in `modules[]`, each naming the section,
  table, or figure that shows the fit.
- `summarization_metadata.conversion_reference`: copy `file`, `converted_at`,
  and `converter_tool` from the `_marked.md` frontmatter.

---

## 7. Prohibited behaviors

- Do not write or edit `review/literature-review-matrix.md`,
  `review/data/quotes.csv`, `review/data/effects.csv`, or any other file under
  `review/`. All of it is generated by `scripts/build_matrix.py`.
- Do not emit a markdown table row. The 56-column format is retired, and the
  current matrix is 15 columns built from your JSON.
- Do not invent DOIs, years, venues, page numbers, sample sizes, statistics, or
  quotes.
- Do not cite a module id absent from `config/taxonomy.yaml`, in either
  `modules[]` or `quotes[].module`.
- Do not write `topic_tags` or `topic_relevance`. Both are retired; module
  assignment replaced them. A summary carrying either is flagged by validation.
- Do not merge several results into one `effects[]` value, or several quotes
  into one record.
- Do not summarize the whole paper in `tldr` and leave the rest empty.
- Do not add a key not in the schema. If the schema cannot express something
  you need, report that instead of inventing a field.
- Do not leave a documented discrepancy out of `effects[]` while keeping the
  claim in `limitations` — validation will fail the summary.
- Do not mark a paper extracted with an empty `modules[]`. Either assign the
  modules it covers, or leave the paper unextracted.

---

## 8. Pre-output self-check (silent)

1. File parses as JSON.
2. Every schema key present.
3. `title`, `authors`, `year`, `venue`, `doi` match `metadata.json`. Comparison is
   case-insensitive and a `https://doi.org/` prefix on the DOI is equivalent —
   anything else is an error, and `metadata.json` wins.
4. Every module id in `modules[]` and `quotes[].module` exists in
   `config/taxonomy.yaml`, and `module_rationale` has one clause per id.
5. `topic_tags` and `topic_relevance` are absent.
6. Every quote is verbatim, `<=40` words, and has a locator and a valid module.
7. Every `effects[]` `outcome` is specific enough to distinguish its row.
8. Every figure quoted in a discrepancy `limitations` entry also appears in
   `effects[]`.
9. `tldr` `<=50` words; `remember_this` items `<=20` words; `claims` `<=30` words.
10. Every substantive claim has a locator.

Then confirm:

```bash
cd Literature && .venv/bin/python -c "import json,sys; d=json.load(open(sys.argv[1])); print('ok', len(d.get('quotes',[])), 'quotes', len(d.get('effects',[])), 'effects')" \
  literature/conversions/{stem}_summarized.json
python3 scripts/build_matrix.py
```

The build must report **0 errors**. Gaps are informational and expected; errors
mean the summary contradicts the corpus and must be fixed.
