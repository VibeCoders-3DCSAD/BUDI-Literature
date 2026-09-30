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
  "topic_tags": ["string — topic codes, max 20"],
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
  "topic_relevance": {
    "topics": [
      {
        "code": "string",
        "name": "string",
        "relevance": "high | medium | low | contextual",
        "justification": "string"
      }
    ],
    "contribution_to_field": "string — 3-5 sentences",
    "directly_justifies": ["string — citable claims, <=30 words each"],
    "limits": ["string — or 'None identified.'"],
    "topic_mapping_rationale": "string — paragraph"
  },
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
      "theme": "string — module id from config/modules.yaml"
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

## Relevance Levels

| Level | Definition |
|-------|-----------|
| `high` | Directly addresses the core concern of the topic |
| `medium` | Provides supporting evidence or contextual example |
| `low` | Tangentially related, mentions topic in passing |
| `contextual` | Background framing only, no actionable insight |

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
- `topic_relevance.topic_mapping_rationale`: Must explicitly state that all topic domains were systematically scanned.
- `citations`: Maximum 15 entries. Each `claim` must be specific and <=30 words.
- `summarization_metadata.conversion_reference`: Populated from the YAML frontmatter of the source `_marked.md` file.

## Extraction Fields

Added 2026-09-30 so the generated matrix
(`docs/literature-review-matrix.md`, schema in `docs/standards/matrix-format.md`)
can be built without a 56-column table. **All of these keys are optional.** A
summary written before this revision stays valid, and a summary may omit any of
them; the builder then renders `Not reported` for that column.

| Key | Feeds matrix column | Notes |
| :--- | :--- | :--- |
| `study_design` | `design` | Use the paper's own label. Normalize to `method/<slug>` in the matrix tag. |
| `sample` | `sample` | N and unit together, as reported. |
| `context` | — | Retained for synthesis; not a matrix column. |
| `software` | — | Retained for reproducibility checks. |
| `quotes[]` | `scores/quotes.json` | One verbatim quotation per record, not a run-on cell. |
| `effects[]` | `scores/effects.json` | One statistical result per record. |

### Field Rules for Extraction Fields

- `quotes[].text` is verbatim, `<=40` words, in straight double quotes. Every
  quote carries a `locator`. `theme` must be a module id that exists in
  `config/modules.yaml`; an invented id is a validation error.
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
{stem}_summarized.json
```

Example: `Cabalfin et al_summarized.json`

## Legacy Formats

YAML (`.yaml`) and Markdown (`.md`) summaries were removed with the `literature/archive/` migration; all summaries are produced as JSON.
