> **Deprecated.** This document is superseded by `docs/standards/note-format.md`.
> Retained for historical reference only.
>
> The `_summarized.json` extraction schema described below no longer exists. The
> schema here is still the source of truth for `modules[]` and
> `module_rationale`, which carried over unchanged into note frontmatter; every
> other key belongs to a file format that was removed on 2026-09-30.

# RRL Summary Format

Reference for the structured JSON summary schema. Summaries are produced in `literature/` (intake) and stored with their `_marked.md` pair in **BUDI-Literature** (`literature/conversions/`).

## Schema

```json
{
  "paper_id": "string — DOI (10.XXXX/...) or UUIDv5, never null",
  "designation": "local | international | local-algorithm-specific | international-algorithm-specific",
  "title": "string",
  "authors": "string — 'Last, F.; Last, F.' or 'Unknown'",
  "year": 0,
  "venue": "string — full name or 'Unknown'",
  "modules": ["string — module ids from config/taxonomy.yaml, max 20"],
  "module_rationale": { "<module id>": "string — one clause naming the section/table/figure that shows the fit" },
  "tldr": "string — one sentence, max 50 words, no 'This paper' start",
  "problem_and_motivation": "string — max 3 sentences, no methodology",
  "approach": ["string — each <=50 words, max 10 items"],
  "findings": ["string — prefix quantitative with 'num: ', max 10 items"],
  "key_figures_tables": ["string — 'Figure X: description → takeaway'"],
  "key_equations": [{"equation": "string", "explanation": "string — <=15 words"}],
  "definitions": [{"term": "string", "definition": "string"}],
  "citations": [
    {
      "author": "string",
      "year": 0,
      "page": 0,
      "paragraph": 0,
      "claim": "string — <=30 words",
      "role": "methodology | finding | baseline | critique | context"
    }
  ],
  "limitations": ["string — use '[unacknowledged]' suffix if needed"],
  "remember_this": ["string — key takeaways, <=20 words, 3-5 items"],
  "study_design": "string — design label as the paper states it, e.g. 'Systematic review'",
  "sample": "string — N and unit as reported, e.g. 'n = 32,581 loan records'",
  "context": {
    "geography": "string — country/region, or 'Not reported'",
    "population": "string — population studied, or 'Not reported'",
    "setting": "string — institutional or virtual setting, or 'Not reported'"
  },
  "software": ["string — named tools/packages with versions, or 'Not reported'"],
  "quotes": [
    {
      "text": "string — verbatim, <=40 words",
      "locator": "string — 'p. 7', 'Abstract', 'Table 3'",
      "module": "string — module id from config/taxonomy.yaml"
    }
  ],
  "effects": [
    {
      "outcome": "string — what was measured",
      "metric": "string — accuracy, RMSE, OR, r, etc.",
      "value": "string — exactly as printed, e.g. '95.21%'",
      "ci": "string — e.g. '+/-2.1%', or omit if unreported",
      "p": "string — e.g. '<0.05', or omit if unreported",
      "locator": "string — 'Table 3', 'Sec. 5'"
    }
  ],
  "summarization_metadata": {
    "summarized_at": "ISO-8601 timestamp",
    "summarizer_model": "string",
    "conversion_reference": {
      "file": "string — source _marked.md filename",
      "converted_at": "ISO-8601 timestamp or null",
      "converter_tool": "string or null"
    }
  }
}
```

## Designation Decision Tree

1. Does the paper's primary contribution involve a specific algorithm, model, or computational technique?
   - **Yes**: proceed to step 2
   - **No**: proceed to step 3
2. Was the study conducted under a Philippine institution or uses Philippine data?
   - **Yes**: `local-algorithm-specific`
   - **No**: `international-algorithm-specific`
3. Is the paper authored under a Philippine institution or focused on the Philippines?
   - **Yes**: `local`
   - **No**: `international`

## Module Assignment

`config/taxonomy.yaml` is the single source of truth: 20 module ids across the 5
outline sections `pfm`, `pfm_apps`, `algorithms`, `methodology`, `evaluation`.

| Field | Rule |
| :--- | :--- |
| `modules[]` | Every module the paper genuinely studies. Ids copied verbatim from the taxonomy; an invented id is a validation error. |
| `module_rationale` | One clause per assigned id, citing the section, table, or figure that shows the fit. |
| `quotes[].module` | Same id namespace, so quotes and paper assignments stay comparable. |

There is **no relevance score, weight, tier, or priority** anywhere in the
schema. Module assignment is a routing decision — where the paper sits in the
outline — not a verdict on the paper's quality or importance. The four BUDGIE
algorithms are first-class modules (`sarima`, `rule_based_classification`,
`linear_programming`, `interquartile_range`); a paper implementing one of them
always gets that module, plus `model_algorithm_integration` if it also wires the
algorithm into a system.

Full decision rules and worked examples: `skills/literature-review-summarizer.md` §5a.

### Retired Fields

| Retired | Replaced by |
| :--- | :--- |
| `topic_tags` | `modules[]` |
| `topic_relevance` (`topics[]`, `relevance`, `contribution_to_field`, `directly_justifies`, `limits`, `topic_mapping_rationale`) | `modules[]` + `module_rationale` |
| `quotes[].theme` | `quotes[].module` |

`scripts/build_matrix.py` still *reads* these keys so the two summaries written
before the taxonomy change are not lost, and it reports any that it finds as an
informational gap telling you to re-tag the paper. Do not write them.

## Citation Roles

| Role | Definition |
|------|-----------|
| `methodology` | Cited work provides the method, framework, or approach |
| `finding` | Cited work provides a specific empirical result |
| `baseline` | Cited work serves as comparison or prior art |
| `critique` | Cited work challenges or qualifies the paper's claims |
| `context` | Cited work provides background or motivation |

## Field Rules

- `tldr`: One sentence, max 50 words. Never starts with "This paper" or "The authors."
- `problem_and_motivation`: Max 3 sentences. No methodology.
- `approach`: Each item <=50 words, ends with period. Max 10 items.
- `findings`: Prefix quantitative results with `"num: "`. Max 10 items.
- `remember_this`: 3-5 items, each <=20 words. No emojis, no numbering.
- `citations`: Maximum 15 entries. Each `claim` must be specific and <=30 words.
- `module_rationale`: Keyed by module id; one clause per entry in `modules[]`.
- `summarization_metadata.conversion_reference`: Populated from the YAML frontmatter of the source `_marked.md` file.

## Extraction Fields

Added 2026-09-30 so the generated matrix
(`review/literature-review-matrix.md`, schema in `docs/standards/review-layout.md`)
can be built from these summaries instead of a 56-column table. **All of these
keys are optional except `modules[]` and `module_rationale`.** A summary written
before this revision stays readable — the builder renders `Not reported` for a
missing column — but a new extraction must assign modules.

| Key | Feeds matrix column | Notes |
| :--- | :--- | :--- |
| `modules[]` | `modules`, `section` | Required. Ids from `config/taxonomy.yaml`. |
| `module_rationale` | — | Required. One clause per id. |
| `study_design` | `design` | Use the paper's own label. |
| `sample` | `sample` | N and unit together, as reported. |
| `tldr` | `key_finding` | One-sentence result statement. |
| `limitations[0]` | `gap` | The paper's own most significant acknowledged limitation. |
| `context` | — | Retained for synthesis; not a matrix column. |
| `software` | — | Retained for reproducibility checks. |
| `quotes[]` | `review/data/quotes.csv` | One verbatim quotation per record, not a run-on cell. |
| `effects[]` | `review/data/effects.csv` | One statistical result per record. |

### Field Rules for Extraction Fields

- `quotes[].text` is verbatim, `<=40` words, in straight double quotes. Every
  quote carries a `locator`. `module` must be an id that exists in
  `config/taxonomy.yaml`; an invented id is a validation error.
- `effects[].value` reproduces the printed number exactly. Do not round,
  recompute, or convert units. `ci` and `p` are omitted rather than guessed.
- **One record per result.** A paper reporting two accuracy figures for two
  conditions gets two records, not one cell containing both.
- When a paper reports the same `metric` twice with different values, keep both
  records with their locators and state the discrepancy in `limitations`. Do not
  silently prefer one. `A--Aldrees-2025` is the worked example: 14.03% in the
  abstract against 14.82% in the conclusion, both genuine.
- `limitations[0]` is what the matrix `gap` column shows, so the first entry
  should be the paper's own most significant acknowledged limitation.

## Summary File Naming

```
{stem}_summarized.json}
```

Example: `literature/conversions/A--Abdullahi-2025_summarized.json` — prefix,
bibliographic first author, year, per `docs/standards/rrl-naming-conventions.md`.

## Legacy Formats

YAML (`.yaml`) and Markdown (`.md`) summaries were removed with the
`literature/archive/` migration; all summaries are produced as JSON. The
17-column JSON schema and the scoring-oriented fields that accompanied it were
retired on 2026-09-30 when `config/modules.yaml` was replaced by
`config/taxonomy.yaml`.
