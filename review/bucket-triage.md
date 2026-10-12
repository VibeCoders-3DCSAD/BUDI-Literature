# Bucket triage and intake handoff

Date: 2026-10-12. Authored record (the builder never touches this file).

`bucket/` at the repository root holds freshly downloaded PDFs awaiting triage.
This record covers one triage pass: what the bucket contained, which items were
taken into the corpus, which were deferred, and what the outstanding note-writing
work is.

## Bucket census

| Count | What |
| :--- | :--- |
| 143 | PDFs |
| 4 | HTML pages (Metrobank 2022, Rizal Commercial Banking Corporation 2024, Financial Planning Association, Tamplin 2024) |
| 71 | PDFs already in the corpus (SHA-256 matches an existing entry) |

The 71 duplicates were confirmed by content hash, not by filename, because
several bucket files carry a different name for a document already held (for
example the bucket `Annual Report 2025` file and the corpus `L--BangkoSentral-2025`).
Those 71 are redundant and can be discarded from the bucket.

The remaining 72 PDFs were genuinely new. A first pass took seven of them into
the corpus; the other 65 are deferred (listed below).

## Intaken (7)

These were staged into `literature/pdfs/`, converted into `literature/mds/`, and
given `metadata.json` entries. Each now has a note stub in `review/notes/` and is
waiting for a full extraction.

| Stem | Title | Conversion | Pages | DOI | Suggested modules |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `I--OECD-2023` | OECD/INFE 2023 International Survey of Adult Financial Literacy | `Organisation for Economic Co-operation and Development, 2023_marked.md` | 76 | 10.1787/56003a32-en | financial_planning; savings_debt_management; income_expense_management |
| `I--NIST-2024` | AI Risk Management Framework: Generative AI Profile (NIST AI 600-1) | `National Institute of Standards and Technology, 2024_marked.md` | 64 | 10.6028/NIST.AI.600-1 | software_quality_evaluation |
| `I--Fenig-2024` | Dynamic Optimization Meets Budgeting: Unraveling Financial Complexities | `Fenig & Petersen, 2024_marked.md` | 99 | 10.3386/w32821 | budgeting; financial_planning |
| `L--BangkoSentral-2021a` | 2021 Financial Inclusion Survey | `Bangko Sentral ng Pilipinas, 2021a_marked.md` | 101 | — | savings_debt_management; income_expense_management; financial_planning |
| `L--BangkoSentral-2021b` | Consumer Finance Survey Report 2021 | `Bangko Sentral ng Pilipinas, 2021b_marked.md` | 267 | — | savings_debt_management; income_expense_management; data_collection |
| `L--BangkoSentral-2026c` | Report on Economic and Financial Developments: Second Quarter 2026 | `Bangko Sentral ng Pilipinas, 2026d_marked.md` | 59 | — | income_expense_management; data_collection |
| `L--BangkoSentral-2026d` | Consumer Expectations Survey Report: 3rd Quarter 2026 | `Bangko Sentral ng Pilipinas, 2026e_marked.md` | 24 | — | income_expense_management; savings_debt_management; data_collection |

The suggested modules are a starting point for the extractor, not a decision: the
note's `modules[]` frontmatter is set during extraction against
`config/taxonomy.yaml`.

### Why these seven

They are the reserved gap-fillers from the priority pass. The OECD and BSP
surveys are primary data on how households plan, save, and borrow; the BSP
quarterly reports continue the local time series that `L--BangkoSentral-2026a`
and `L--BangkoSentral-2026b` already start; NIST AI 600-1 is the one document in
the bucket that speaks to software quality and risk; and Fenig and Petersen is a
direct study of budgeting under optimisation.

### Stems that do not match their file letters

The corpus binds each stem to its files through `metadata.json`, so a stem's
letter suffix need not match the source PDF's. Two pairs here differ:

- `L--BangkoSentral-2021a` (Financial Inclusion Survey) is bound to
  `Bangko Sentral ng Pilipinas, 2021a.pdf`.
- `L--BangkoSentral-2021b` (Consumer Finance Survey) is bound to
  `Bangko Sentral ng Pilipinas, 2021b.pdf`.
- `L--BangkoSentral-2026c` (Q2 2026 report) is bound to
  `Bangko Sentral ng Pilipinas, 2026d.pdf`.
- `L--BangkoSentral-2026d` (CES Q3 2026) is bound to
  `Bangko Sentral ng Pilipinas, 2026e.pdf`.

## Deferred (65)

Not taken in this pass. They were not individually assessed; this is a park list,
not a rejection. Year is not a reason to drop an item (the citation window is
permissive for on-topic primary data), so the list is a queue for a later pass.

```
Albert et al., 2024                 Altalhan et al., 2025        Am-una, 2026
Anes & Abreu, 2025                  Apus et al., 2023            Aquino et al., 2025
Asebedo, 2025                       Azamuke et al., 2025         Bakuwa & Jimu
Bari et al                          Carmona, 2025                Celestin et al., 2025
Chandana et al                      Chen V. et al                Claros et al., 2026
Comia, 2024                         Consumer Financial Protection Bureau, 2015
Enache et al., 2023                 Fariha et al                 Fathy
Financial Planning Association, n.d.  Flores, 2025              Haimson et al., 2021
Hambala & Maquiling, 2025           Hartomo et al                Hernadez et al., 2023
Hossain et al                       Hovakimyan & Bravo           Japinye & Adedugbe
Jumady et al., 2024                 Kanalakis, 2023              Khashadourian & Harrison, 2024
Kowsar M. et al-2023                Lockwood et al               Malave et al
Mashiko et al., 2025                Metrobank, 2022              Mienye et al-2026
Nagaraj                             Ng et al                     Nie et al
Pandiin & Matias                    Prades, 2025                 Rafiaei
Razalan, n.d.                       Rizal Commercial Banking Corporation, 2024
Santiago, 2026                      Schlechter et al., 2026      Schwartz
Scrivano A.-2025a                   Tadeja et al., 2024          Tamplin, 2024
Tjostheim                           Tun, 2023                    Wiranatakusuma et al., 2024
Yunita et al                        Зарубежный

Bangko Sentral ng Pilipinas, 2019 (image-only, 2 pages)
Bangko Sentral ng Pilipinas, 2025a (Annual Report 2025, 142 pages — broad)
Bangko Sentral ng Pilipinas, 2026c (DepEd financial-planning module)
Bangko Sentral ng Pilipinas, n.d.(c) (Personal Financial Management booklet)
```

## Already covered (not intake)

The four PSA quarter releases in the bucket (`Philippine Statistics Authority,
2025a/c/d` and `2026a`) are already inside the corpus. The existing
`L--PSA-2025` conversion concatenates all four 2025 quarter releases, and
`L--PSA-2026` concatenates Q1 and Q2 2026. Taking the individual files would
duplicate the series, so they were left in the bucket.

## Handoff: writing the notes

The note-writing is outsourced. For each of the seven intaken papers, feed the
conversion in `literature/mds/` to an extraction agent and have it follow:

- `skills/literature-review-summarizer.md` — the output contract.
- `docs/standards/note-format.md` — the note grammar.

The agent writes the whole file at `review/notes/{stem}.md`. The builder never
overwrites a note that exists, so a finished note replaces its stub.

When a batch of notes is ready, verify each and rebuild:

```bash
python3 scripts/qc_note.py {stem}          # per-note depth and structural gate
python3 scripts/build_matrix.py --check     # corpus-wide; exits 1 on any error
```
