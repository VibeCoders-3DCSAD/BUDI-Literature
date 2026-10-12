# RRL Processing Workflow

Workflow for adding and processing literature in the Review of Related Literature.

All steps happen within **BUDI-Literature**. No cross-repo transfers required.

Six steps: fetch, convert, extract, build, verify, adapt. There is no scoring
step — module coverage is decided during extraction (step 3), not computed
afterwards from text similarity.

## Steps

### 1. Fetch PDFs

Obtain source PDFs from a local archive or remote source:

```bash
# From a sibling directory (e.g. BUDI-Base/archived-literature/pdfs/):
python3 scripts/fetch_pdfs.py --source local --path ../BUDI-Base/archived-literature/pdfs/

# From a .zip archive:
python3 scripts/fetch_pdfs.py --source local --path /path/to/pdf-archives/

# From a remote URL:
python3 scripts/fetch_pdfs.py --source remote --url https://example.com/papers.zip
```

PDFs are placed in `literature/pdfs/` (gitignored). The script computes SHA-256 hashes for each PDF.

Optional: inspect fetched PDFs before converting:

```bash
python3 scripts/count_pdf_pages.py literature/pdfs/
python3 scripts/count_pdf_pages.py literature/pdfs/ --lte 20   # only short papers
python3 scripts/check_dupe_pdfs.py literature/pdfs/ --cascade  # find duplicates
```

### 2. Convert

Run the PDF-to-Markdown converter:

```bash
python3 scripts/prepare_pdf.py literature/pdfs/ --page-aware
```

Produces `{pdf-name}_marked.md` (the PDF name plus `_marked.md`) with YAML
frontmatter (conversion metadata, SHA-256 hash, page count). Move it into the
corpus root:

```bash
mv literature/pdfs/{pdf-name}_marked.md literature/mds/
```

Options: `--page-aware` adds `<!-- PAGE N -->` markers via pdfminer.six;
`--json-sidecar` writes a separate `{stem}_conversion_meta.json`. The corpus is
flat; do not create per-intake subdirectories. See
`docs/standards/rrl-naming-conventions.md`.

The conversion is named after the PDF, not the stem, so it is the **sidecar** that
binds them. For each new paper, verify the first author and year against page 1 of
the PDF (source filenames often name a later author), choose the canonical stem
`{Prefix}--{AuthorLastName}-{Year}`, and add an entry to
`literature/mds/metadata.json` keyed by that stem, recording `source_pdf`,
`source_pdf_path`, and `conversion_md`. The builder resolves every paper through
those fields; a conversion the sidecar does not list is ignored.

### 3. Extract into a note

Use an AI agent to write `review/notes/{stem}.md`, the authored extraction record
for the paper. Feed the agent the corresponding `_marked.md` file.

The extractor is **objective and unbiased** — it describes what the paper says
without application-specific framing. Page and paragraph references are included
as locators.

See `docs/standards/note-format.md` for the note schema, and
`skills/literature-review-summarizer.md` for the output contract.

Two fields carry the weight of the whole pipeline:

- **`modules[]`** — the frontmatter ids from `config/taxonomy.yaml` this paper
  genuinely covers, each with a `module_rationale` clause. Every coverage count
  in the matrix is a tally of these assignments. A note with an empty
  `modules[]` is an incomplete extraction.
- **`## Statistical Evidence` / `## Quotes`** — one record per statistical result
  and per quotation. A paper that reports the same measurement twice with
  different numbers keeps **both** records with their locators and states the
  discrepancy in `## Limitations and Gaps`; never reconcile silently.

Bibliographic fields (`title`, `authors`, `year`, `venue`, `doi`) are copied from
`literature/mds/metadata.json`, the page-1-verified citation authority.
The agent does not re-derive them. The builder never overwrites a note that
already exists; it creates a stub only for a paper that has none.

### 4. Build the review matrix

```bash
python3 scripts/build_matrix.py           # build the whole review/ tree
python3 scripts/build_matrix.py --check   # validate only, exit 1 on any error
```

Inputs: `metadata.json` (bibliographic authority), every `review/notes/*.md`
(extraction), and `config/taxonomy.yaml` (module namespace). Outputs:

| File | Contents |
|------|----------|
| `review/literature-review-matrix.md` | 15-column index, one row per corpus paper, plus a per-module coverage view. |
| `review/data/papers.csv` | The 15 columns plus a controlled `tags` column. |
| `review/data/screening.csv` | Intake triage: status, module count, DOI and venue completeness. |
| `review/data/quotes.csv` | One record per extracted quotation. |
| `review/data/effects.csv` | One record per statistical result. |
| `review/data/themes.csv` | Per-module coverage tally. |
| `review/notes/{stem}.md` | A stub for each paper that has no note; authored notes are left untouched. |
| `review/validation.md` | Validation errors and informational gaps. |

**Never hand-edit the matrix, the CSVs, or `validation.md`, and never overwrite an
authored note.** Fix the source and rebuild. Column definitions, the tag
namespace, and every validation rule are in `docs/standards/review-layout.md`.

### 5. Verify

```bash
python3 scripts/build_matrix.py --check
```

Read the gap list before requesting new sources — a module showing zero papers is
the evidence for what to go and find. Gaps are informational and never fail the
build; **errors** mean the corpus contradicts itself and must be fixed.

The per-module tally to read is `review/data/themes.csv`; the intake queue is
`review/data/screening.csv`.

### 6. Adapt to Thesis Changes

The thesis outline, architecture, and algorithm selections change often. When the
outline changes, edit **only** `config/taxonomy.yaml` and re-tag the notes'
frontmatter `modules[]`; no code changes are needed.

Renaming a module is not free: ids are stored in every note's frontmatter
`modules[]` and in the `Module` column of each `## Quotes` table, so after a
rename the corpus keeps reporting the old namespace until the notes are
retagged.

## Python Dependencies

Install from repository root:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

| Package | Required By |
|---------|------------|
| `markitdown` | `prepare_pdf.py` |
| `pypdf` | `count_pdf_pages.py`, `prepare_pdf.py` (--page-aware) |
| `PyPDF2` | `check_dupe_pdfs.py` |
| `pdfminer.six` | `prepare_pdf.py` (--page-aware) |
| `PyYAML` | `build_matrix.py` (reads `config/taxonomy.yaml`) |

`scripts/check_dupe_pdfs.py` also uses PyMuPDF, Pillow, and ImageHash for its
perceptual-hash tier. They are optional: the script falls back to a SHA-256 +
text-similarity cascade when they are not installed. Uncomment them in
`requirements.txt` to enable the visual tier.

## Intake Runbook

Repeatable checklist for a batch of staged PDFs. Run it per batch.

```bash
# 0. PDFs staged flat in literature/pdfs/ (moved from bucket/)
# 1. inspect
python3 scripts/count_pdf_pages.py literature/pdfs/
python3 scripts/check_dupe_pdfs.py literature/pdfs/ --cascade
# 2. convert + move
python3 scripts/prepare_pdf.py literature/pdfs/ --page-aware
mv literature/pdfs/{pdf-name}_marked.md literature/mds/
# 3. add a metadata.json entry per new paper, then extract each conversion into a note (agent; modules[] is required)
# 4. rebuild
python3 scripts/build_matrix.py
# 5. verify
python3 scripts/build_matrix.py --check
```

> Note: `prepare_pdf.py` scans only the flat `literature/pdfs/` top level for
> `.pdf`. Keep PDFs there directly, not in subdirectories, or they will be skipped.

Run step 4 after anything that changes a stem, a conversion, bibliographic
metadata, or a note. The build is idempotent, so re-running it is always safe.

## Script Reference

| Script | Purpose |
|--------|---------|
| `scripts/fetch_pdfs.py` | Fetch PDFs from local archive or remote source |
| `scripts/prepare_pdf.py` | Convert PDFs to Markdown with metadata |
| `scripts/count_pdf_pages.py` | List PDFs with page counts |
| `scripts/check_dupe_pdfs.py` | Find duplicate PDFs by hash cascade |
| `scripts/build_matrix.py` | Build the generated matrix, long tables, and validation report, and write note stubs for papers that have no note |
| `scripts/common.py` | Shared helpers (corpus paths, text cleaning, frontmatter parsing) |
