# Literature Review Layout

`review/` mixes an authored surface with a generated one. `review/notes/` and
`review/synthesis/` are **authored**: the builder never overwrites a note that
exists. The matrix, `review/data/*.csv`, and `review/validation.md` are
**generated** by `scripts/build_matrix.py` and must never be hand-edited.

```bash
python3 scripts/build_matrix.py           # rebuild the generated review/ files
python3 scripts/build_matrix.py --check   # validate only, exit 1 on any error
```

The rebuild reads exactly three sources:

| Source | Role |
| :--- | :--- |
| `literature/conversions/metadata.json` | Bibliographic authority. Page-1 verified; overrides note frontmatter. |
| `review/notes/*.md` | Authored extraction. Supplies every non-bibliographic column. |
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
    {stem}.md                   authored — one extraction note per paper (stub if none)
  synthesis/                    authored — hand-written cross-paper synthesis
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
| `modules` | note frontmatter `modules[]` | Ids joined with `; `, ordered by taxonomy order. |
| `design` | note `**Design.**` line | The paper's own label. |
| `sample` | note `**Sample.**` line | N and unit together. |
| `key_finding` | note `## Summary` | One sentence. |
| `gap` | note `## Limitations and Gaps` (first bullet) | The paper's own most significant limitation. |
| `status` | note frontmatter `status` | `extracted` or `not extracted`. |

Every empty cell renders as `Not reported`, never blank and never `N/A`.

`papers.csv` carries these 15 columns plus a `tags` column (a controlled
`namespace/value` string) used for filtering. `tags` is **not** a matrix column.

---

## Module assignment

Coverage is a count of assignments, nothing else:

- `modules[]` in a note's frontmatter holds ids copied verbatim from `config/taxonomy.yaml`.
- `data/themes.csv` and the matrix's coverage table tally papers per module.
- A module with zero papers is a **gap in the corpus**, not a defect in the
  taxonomy and not a reason to loosen assignment.
- There is no relevance score, weight, tier, or priority. A paper appearing in a
  module is a routing fact, not a quality judgement.

Assignment rules: `docs/standards/note-format.md` §Frontmatter.

---

## Per-paper notes

`review/notes/{stem}.md` is the authored extraction record for one paper:
frontmatter, then a summary, problem, method, software, key findings, a
statistical-evidence table, limitations, and a link back to the conversion. The
builder reads the note and never rewrites it: it writes a stub only for a paper
that has no note, and that stub says so and links to the extraction contract.

Because notes are authored, they are the source that the generated matrix and
CSVs are derived from — fix a note, not the matrix. Prose that belongs to a human
— cross-paper comparison, argument, narrative — goes in `review/synthesis/`, which
nothing overwrites.

---

## Validation

`--check` and every full build report **errors** and **gaps** separately.

**Errors** mean the corpus contradicts itself and the build should fail. The
retained topic-independent rules are:

| Error | Meaning |
| :--- | :--- |
| Unknown stem | A note or conversion has no `metadata.json` entry. |
| Bibliographic mismatch | Note title/authors/year/venue/DOI disagree with the sidecar. |
| Invented module | A `modules[]` or `## Quotes` `Module` id is absent from `config/taxonomy.yaml`. |
| Discrepancy not recorded | A figure named in a `## Limitations and Gaps` entry is missing from `## Statistical Evidence`. |

**Gaps** are informational and never fail the build: unassigned modules,
unassigned papers, missing DOIs, unverified venues, absent publication types,
author/year collisions, and suppressed fill-rate verdicts while fewer than 10
papers are extracted.

`validation.md` is the human-readable report of the same run.

---

## Regeneration guarantees

- Two consecutive builds are byte-identical apart from the `generated`
  timestamp. CSV and generated-stub output is byte-identical with no exceptions.
- The builder creates `review/data/` and `review/notes/` if missing. It writes a
  stub for a paper with no note, never overwrites an existing note, and removes a
  note whose stem has left the corpus, so the tree cannot drift.
- `--check` performs no writes.

## Changing a value

Fix the source, then rebuild. Never edit a generated file under `review/`
directly; edit the note it is derived from and let the build regenerate the rest.

| To change | Edit |
| :--- | :--- |
| A bibliographic value | `literature/conversions/metadata.json` |
| A finding, gap, or module | `review/notes/{stem}.md` (authored) |
| The set of modules | `config/taxonomy.yaml` |
| A column definition | this file, and the constants in `scripts/build_matrix.py` |
