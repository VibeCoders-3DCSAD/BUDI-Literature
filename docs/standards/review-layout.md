# Literature Review Layout

`review/` is a **generated view** of the corpus, not a database. Everything in it
except `review/synthesis/` is rebuilt by `scripts/build_matrix.py` and must never
be hand-edited.

```bash
python3 scripts/build_matrix.py           # rebuild review/
python3 scripts/build_matrix.py --check   # validate only, exit 1 on any error
```

The rebuild reads exactly three sources:

| Source | Role |
| :--- | :--- |
| `literature/conversions/metadata.json` | Bibliographic authority. Page-1 verified; overrides conversion frontmatter. |
| `literature/conversions/{stem}_summarized.json` | Extraction. Supplies every non-bibliographic column. |
| `config/taxonomy.yaml` | Module namespace. Defines the valid `modules[]` ids. |

Nothing else feeds the matrix. In particular there is no score file, no
embedding cache, and no corpus manifest: coverage comes from module assignment
made during extraction, not from a similarity search.

---

## Tree

```
review/
  literature-review-matrix.md   generated — the browsable 15-column index
  validation.md                 generated — errors and informational gaps
  data/
    papers.csv                  one row per paper, the matrix columns + tags
    screening.csv               triage view for the intake queue
    quotes.csv                  one row per extracted quotation
    effects.csv                 one row per statistical result
    themes.csv                  per-module coverage tally
  notes/
    {stem}.md                   one note per paper
  synthesis/                    hand-written — the only authored part of review/
```

`review/data/*.csv` is the machine-readable surface; the matrix is the human
surface. They are generated together, so they never disagree.

---

## Matrix columns

`review/literature-review-matrix.md` has 15 columns in this fixed order.

| Column | Source | Rule |
| :--- | :--- | :--- |
| `paper_id` | stem | Never empty. Primary key across every table. |
| `first_author` | `metadata.json` | Falls back to the stem when metadata omits it. |
| `year` | `metadata.json` | Integer, or the literal the source prints. |
| `title` | `metadata.json` | Never re-derived from the PDF. |
| `venue` | `metadata.json` | `Unverified: <reason>` when the sidecar flags it. |
| `doi` | `metadata.json` | Normalised; a line-broken DOI is rejoined at the source. |
| `type` | `metadata.json` | Publication type, or `Not reported`. |
| `designation` | stem prefix | Derived from the `L--` / `I--` / `A--` prefix, never from content. |
| `section` | `taxonomy.yaml` | Human-readable outline section(s) implied by `modules`. |
| `modules` | summary `modules[]` | Ids joined with `; `, ordered by taxonomy order. |
| `design` | summary `study_design` | The paper's own label. |
| `sample` | summary `sample` | N and unit together. |
| `key_finding` | summary `tldr` | One sentence. |
| `gap` | summary `limitations[0]` | The paper's own most significant limitation. |
| `status` | derived | `extracted` or `not extracted`. |

Every empty cell renders as `Not reported`, never blank and never `N/A`.

`papers.csv` carries these 15 columns plus a `tags` column (a controlled
`namespace/value` string) used for filtering. `tags` is **not** a matrix column.

---

## Module assignment

Coverage is a count of assignments, nothing else:

- `modules[]` in a summary holds ids copied verbatim from `config/taxonomy.yaml`.
- `data/themes.csv` and the matrix's coverage table tally papers per module.
- A module with zero papers is a **gap in the corpus**, not a defect in the
  taxonomy and not a reason to loosen assignment.
- There is no relevance score, weight, tier, or priority. A paper appearing in a
  module is a routing fact, not a quality judgement.

Assignment rules: `docs/standards/summary-format.md` §Module Assignment.

---

## Per-paper notes

`review/notes/{stem}.md` is the readable form of one summary: frontmatter, then
`tldr`, problem, method, software, key findings, a statistical-evidence table,
limitations, and links back to the conversion and summary JSON. Unextracted
papers get a stub that says so and links to the extraction contract.

Notes are generated, so they stay in step with the JSON. Prose that belongs to a
human — cross-paper comparison, argument, narrative — goes in
`review/synthesis/`, which nothing overwrites.

---

## Validation

`--check` and every full build report **errors** and **gaps** separately.

**Errors** mean the corpus contradicts itself and the build should fail. The
retained topic-independent rules are:

| Error | Meaning |
| :--- | :--- |
| Unknown stem | A summary or conversion has no `metadata.json` entry. |
| Bibliographic mismatch | Summary title/authors/year/venue/DOI disagree with the sidecar. |
| Invented module | A tag or `quotes[].module` id is absent from `config/taxonomy.yaml`. |
| Discrepancy not recorded | A figure named in a `limitations` entry is missing from `effects[]`. |

**Gaps** are informational and never fail the build: unassigned modules,
unassigned papers, missing DOIs, unverified venues, absent publication types,
author/year collisions, and suppressed fill-rate verdicts while fewer than 10
papers are extracted.

`validation.md` is the human-readable report of the same run.

---

## Regeneration guarantees

- Two consecutive builds are byte-identical apart from the `generated`
  timestamp. CSV and note output is byte-identical with no exceptions.
- The builder creates `review/data/` and `review/notes/` if missing and removes
  note files whose stem has left the corpus, so the tree cannot drift.
- `--check` performs no writes.

## Changing a value

Fix the source, then rebuild. Never edit `review/` directly.

| To change | Edit |
| :--- | :--- |
| A bibliographic value | `literature/conversions/metadata.json` |
| A finding, gap, or module | `literature/conversions/{stem}_summarized.json` |
| The set of modules | `config/taxonomy.yaml` |
| A column definition | this file, and the constants in `scripts/build_matrix.py` |
