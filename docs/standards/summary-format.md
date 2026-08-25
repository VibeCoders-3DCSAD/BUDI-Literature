# RRL Summary Format

Reference for the structured JSON summary schema. Summaries are produced in `literature/` (intake) and stored with their `_marked.md` pair in **Odin-Literature** (`literature/conversions/batch-<N>/`). See `literature/_MIGRATION.md`.

Full prompt: `literature/skills/paper-summarizer-skill.md`

## Schema

```json
{
  "paper_id": "string — DOI (10.XXXX/...) or UUIDv5, never null",
  "designation": "local | international | local-algorithm-specific | international-algorithm-specific",
  "title": "string",
  "authors": "string — 'Last, F.; Last, F.' or 'Unknown'",
  "year": 0,
  "venue": "string — full name or 'Unknown'",
  "odin_topics": ["string — topic codes, max 20"],
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

## Summary File Naming

```
{stem}_summarized.json
```

Example: `Cabalfin et al_summarized.json`

## Legacy Formats

YAML (`.yaml`) and Markdown (`.md`) summaries were removed with the `literature/archive/` migration; all summaries are produced as JSON.
