# Citation Audit — Chapter 1 V6, Chapter 2 V4, Chapter 3 V1

```json
{
  "document-type": "citation-audit",
  "version": "1.0.0",
  "date": "2026.10.08"
}
```

Audits every inline citation in the freshest chapter drafts pulled from the Google Drive
mirror against the corpus bibliography (`literature/paper-markdowns/metadata.json` and the 97
`review/notes/` extractions). This is the companion check to `NEW-SCOPE-SOURCES.md`: that file
prioritises what to download; this file says what the current chapters actually cite and
whether the corpus can prove each reference.

## Verdict

Across the three chapters the corpus resolves **32** of the **58** distinct works cited,
holds one standard (ISO 25010:2023), and is missing **25** distinct works. The missing works
cluster in three places:

1. **Chapter 3's classification boundaries are still external.** Four of its five sources
   (Adams et al. 2022, Bhutta et al. 2023, He and Zhou 2022, Tukey 1977) stay unheld; the
   Board of Governors (2024) reference now resolves to `I--FederalReserve-2024`, giving the
   chapter its first corpus-backed source.
2. **Chapter 2's methodological and evaluation tail is external.** Twenty-one of its 53
   distinct works resolve to no corpus entry, including the boxplot/IQR canon (Tukey 1977),
   the SARIMA originals (Box and Jenkins 1970), LP founding (Dantzig 1963), and the SUS
   literature (Brooke 1996, Bangor et al. 2008, Lewis 2018).
3. **Chapter 1's Philippine statistical claims still lean on unheld official series** (BSP
   2024a-d, FSCC 2024). PSA (2025), PSA (2026), and Board of Governors (2024) were converted
   and are now held; these were the official-series gap and its only international report.

Status of the older six-item shortlist from `NEW-SCOPE-SOURCES.md` P0.4: five were still cited
and still unheld at audit time; PSA 2023 has fallen out of the chapter and been replaced by
PSA 2025 and PSA 2026, both now held. Dasmariñas (2024), acquired since, is now held and cited
in both Chapters 1 and 2.

## Method

- **Sources.** Text extracted from `GROUP4 - CHAPTER 1 - V6 - 09.24.26.docx`,
  `GROUP4 - CHAPTER 2 - V4 - 10.01.2026.docx`, and `GROUP4 - CHAPTER 3 - V1 - 09.20.26.docx`
  in `Base/mirror/`, stripped to paragraph text. The `References V1 - 10.06.2026.docx` file is
  an empty stub ("References / Hello world"), so the reference list itself cannot be
  cross-checked and this audit covers inline citations only.
- **Extraction.** Author-year strings were pulled by regex over parenthetical and narrative
  citations, `&amp;` normalised, then each was read individually so that split "Alenazi / Sas"
  and bracketed-institution forms resolve to a single work. Ambiguous strings were checked in
  their surrounding paragraph.
- **Resolution.** A work is **held** only if the author-year string corresponds to a
  `metadata.json` entry with a `review/notes/{stem}.md` file. Resolution was confirmed by
  matching the chapter's quoted claim to the corpus title for a sample of the top-frequency
  references (Lu, de Zarzà, Dasmariñas, Francisco, Santiago, Alenazi, Zhong, Huang,
  Ghonaim, Sapiri).

**Verified:** string-to-corpus resolution for every occurrence, and title-level agreement for
the sample above. **Inferred:** occurrence counts below are token frequencies from the text
(a citation used once in one paragraph still counts once per paragraph), not exact reference
counts; a handful of narrative forms are an approximate count. **Not checked:** paragraph-level
accuracy of every held paper's claims, and whether Chapter 1's statistics attributed to BSP 2026b
match that report's contents (flagged in "Cross-cutting findings").

---

## Chapter 2 V4 (10.01.2026) — the review

53 distinct works: 31 held, 21 unheld, 1 standard.

### Held (31)

| Citation (V4) | Occurrences | Corpus stem |
| :--- | :---: | :--- |
| Lu et al., 2025 | 33 | `A--Lu-2025` |
| de Zarzà et al., 2024 | 29 | `A--DeZarza-2024` |
| Cumaio et al., 2026 | 23 | `I--Cumaio-2026` |
| Gulbakyt et al., 2025 | 23 | `A--Gulbakyt-2025` |
| Francisco et al., 2026 | 18 | `L--Francisco-2026` |
| Santiago et al., 2025 | 16 | `L--Santiago-2025` |
| Huang et al., 2025 | 16 | `A--Huang-2025` |
| Alenazi & Sas, 2023 | 15 | `A--Alenazi-2023` |
| Hamdare et al., 2025 | 15 | `A--Hamdare-2025` |
| Yeo et al., 2023 | 13 | `I--Yeo-2023` |
| Zhong, 2025 | 13 | `A--Zhong-2025` |
| D'Souza et al., 2026 | 12 | `A--DSouza-2026` |
| Ghonaim & El-Sharawy, 2025 | 12 | `A--Ghonaim-2025` |
| Thakur & Jadhav, 2025 | 12 | `A--Thakur-2025` |
| Claro & Noval, 2025 | 11 | `L--Claro-2025` |
| Laspiñas & Murcia, 2024 | 11 | `L--LaspinasMurcia-2024` |
| Esperanza, 2025 | 9 | `L--Esperanza-2025` |
| Samli et al., 2026 | 9 | `I--Samli-2026` |
| BSP, 2026b | 6 | `L--BangkoSentral-2026b` |
| Sapiri & Awaluddin, 2023 | 6 | `I--Sapiri-2023` |
| Yoganandham, 2025 | 5 | `I--Yoganandham-2025` |
| Dasmariñas et al., 2024 | 5 | `L--Dasmarinas-2024` |
| Danahy et al., 2024 | 2 | `I--Danahy-2024` |
| Dey & Arefin, 2025 | 2 | `A--DeyArefin-2025` |
| Ganong et al., 2025 | 1 | `I--Ganong-2025` |
| Yadav et al., 2026 | 1 | `I--Yadav-2026` |
| Vecina & Encarnacion, 2025 | 1 | `L--Vecina-2025` |
| Philippine Statistics Authority, 2025 | 2 | `L--PSA-2025` |
| Philippine Statistics Authority, 2026 | 2 | `L--PSA-2026` |
| Guo et al., 2024 | 1 | `A--Guo-2024` |
| Board of Governors of the Federal Reserve System, 2024 | 1 | `I--FederalReserve-2024` |

Resolution notes: "Santiago" refers to the budget-information-system paper; "Dey & Arefin" to
the rule-based household-budget precedent; "Vecina & Encarnacion" surfaced only once in this
chapter but has a full note and is kept. PSA 2025 and PSA 2026 resolve to the merged
quarterly-HFCE series entries `L--PSA-2025`/`L--PSA-2026` (one series entry per release year).

### Unheld (21)

| Citation (V4) | Occurrences | Note |
| :--- | :---: | :--- |
| Simonse et al., 2024 | 2 | Financial stress / household finances |
| Ariningsih & Muhammad, 2024 | 2 | ISO 25010 evaluation — P0.3 |
| Lianto et al., 2023 | 2 | ISO 25010 evaluation — P0.3 |
| Lim et al., 2025 | 2 | SUS usability review — P0.3 |
| FSCC, 2024 | 2 | Financial Stability Coordination Council — official body |
| Bunyi, 2024 | 1 | Financial resilience among Filipinos |
| Hamid et al., 2023 | 1 | Financial stress components |
| Box & Jenkins, 1970 | 1 | Canonical SARIMA/ARIMA source — pre-2023 |
| Adams et al., 2022 | 1 | Credit-card revolver categories — pre-2023 |
| Bhutta et al., 2023 | 1 | SCF savings/financial literacy |
| He & Zhou, 2022 | 1 | Financial vulnerability — pre-2023 |
| Laaber et al., 2024 | 1 | DMFT/PTM lifecycle instruments |
| Arfani et al., 2022 | 1 | Agile/scrum — pre-2023 |
| Hnatkowska et al., 2022 | 1 | Scrum/Kanban taxonomy — pre-2023 |
| Dantzig, 1963 | 1 | LP founding — pre-2023 |
| Tukey, 1977 | 1 | IQR/boxplot origin — pre-2023 |
| Sathe & Panse, 2023 | 1 | Agile constraints — P0.2 |
| Brooke, 1996 | 1 | SUS instrument — window exception |
| Bangor et al., 2008 | 1 | SUS benchmark — pre-2023 |
| Lewis, 2018 | 1 | Standardised usability questionnaires — pre-2023 |
| Hyndman & Kostenko, 2007 | 1 | Seasonal-sample-size caution — pre-2023 |

### Standard

| Citation (V4) | Occurrences | Note |
| :--- | :---: | :--- |
| ISO/IEC 25010, 2023 | 3 | Standard, admissible under the window exception |

---

## Chapter 1 V6 (09.24.26) — introduction

16 distinct works: 8 held, 8 unheld.

### Held (8)

| Citation (V6) | Corpus stem |
| :--- | :--- |
| Ganong et al., 2025 | `I--Ganong-2025` |
| Yeo et al., 2023 | `I--Yeo-2023` |
| Yadav et al., 2026 | `I--Yadav-2026` |
| D'Souza et al., 2026 | `A--DSouza-2026` |
| Bangko Sentral ng Pilipinas [BSP], 2026b | `L--BangkoSentral-2026b` |
| Bangko Sentral ng Pilipinas, 2026a | `L--BangkoSentral-2026a` |
| Danahy et al., 2024 | `I--Danahy-2024` |
| Dasmariñas et al., 2024 | `L--Dasmarinas-2024` |

### Unheld (8)

| Citation (V6) | Note |
| :--- | :--- |
| BSP, 2024a | Consumer Expectations Survey (Q-range for 2024) |
| BSP, 2024b | Consumer Expectations Survey |
| BSP, 2024c | Consumer Expectations Survey |
| BSP, 2024d | Consumer Expectations Survey |
| Financial Stability Coordination Council [FSCC], 2024 | Official body |
| Hamid et al., 2023 | Financial stress |
| Simonse et al., 2024 | Financial stress |
| Bunyi, 2024 | Financial resilience |

Chapter 1 also cites Dasmariñas et al. (2024) for the pandemic-contraction caution and a CES
cluster for the saving-rate claim; no `L--BangkoSentral-2024*` entries exist in the corpus
(held BSP years are 2023a, 2023b, 2025, 2026a, 2026b).

---

## Chapter 3 V1 (09.20.26) — methodology

5 distinct works: 1 held, 4 unheld. The Board of Governors (2024) reference now resolves to
`I--FederalReserve-2024`, the chapter's first corpus-backed source; the classification
boundaries themselves still rest on external works.

| Citation (V1) | Occurrences | Corpus stem / note |
| :--- | :---: | :--- |
| Board of Governors of the Federal Reserve System, 2024 | 1 | `I--FederalReserve-2024` |
| Adams, Bord, and Katcher, 2022 | 1 | Transactor / light-revolver / heavy-revolver categories (unheld) |
| Bhutta, Blair, and Dettling, 2023 | 1 | Savings/financial-literacy framing (unheld) |
| He and Zhou, 2022 | 2 | Financial-vulnerability framework (DSTI 40% boundary, negative-margin reading) (unheld) |
| Tukey, 1977 | 1 | IQR/boxplot method and the 1.5 multiplier (unheld) |

---

## Cross-cutting findings

1. **Chapter 3's classification boundaries still lack corpus backing.** Its core boundaries
   (40% DSTI, EFC ≥ 3, revolver categories) rest on four external works (Adams et al. 2022,
   Bhutta et al. 2023, He and Zhou 2022, Tukey 1977); the Board of Governors (2024) framing
   now resolves to `I--FederalReserve-2024`. The corpus contains the nearest method precedent,
   `A--DeyArefin-2025` (rule-based household budget), which Chapter 3 does not cite; the
   classifier argument is the thesis's core algorithm and its boundary evidence is still not
   held.
2. **Six pre-2023 works need a window ruling, not just Brooke.** `NEW-SCOPE-SOURCES.md`
   admits only Brooke (1996) as a measurement-instrument exception. Chapter 2 V4 now also cites
   Box and Jenkins (1970), Dantzig (1963), Tukey (1977), Bangor et al. (2008), Lewis (2018),
   and Hyndman and Kostenko (2007), and Chapters 2–3 cite Adams et al. (2022), Arfani et al.
   (2022), Hnatkowska et al. (2022), and He and Zhou (2022). Either the window rule is extended
   (canonical-method, instrument-benchmark) or these citations must change, because the rule as
   written makes them not citable.
3. **Chapter 1's BSP 2026b claim needs a content check.** Chapter 1 attributes the 2025
   Consumer Finance and Inclusion Survey (8,784 interviews; 48% covering one month) to
   "[BSP], 2026b". The corpus keys `L--BangkoSentral-2026b` as the *Q1 2026 Report on Economic
   and Financial Developments*, and tracks a separate unheld BSP (2025) CFIS entry in
   `NEW-SCOPE-SOURCES.md` P1. Verify that the Q1 2026 report is where the survey figures
   actually live; if not, the citation belongs on the CFIS release.
4. **Two official-body citations remain unproven; three are now held.** FSCC (2024) and the
   BSP CES quarterlies (2024a-d) still qualify under the government-report and statistical-series
   exceptions but are not held, so they cannot be verified against the text. PSA (2025), PSA
   (2026), and Board of Governors (2024) were converted on 2026-10-08 (`L--PSA-2025`,
   `L--PSA-2026`, `I--FederalReserve-2024`) and are now verified from page 1.
5. **References V1 is a stub.** `GROUP4 - REFERENCES - V1 - 10.06.2026.docx` contains only the
   heading and "Hello world". Until the reference list is drafted there is no third artifact to
   reconcile against the inline citations.

---

## Corpus housekeeping (2026-10-08)

- **Layout migrated**: `literature/conversions/` → `literature/paper-markdowns/`, `literature/papers/` →
  `literature/paper-pdfs/`. `scripts/common.py`, `scripts/build_matrix.py`, `.gitignore`, and the
  standards docs re-pointed; conversions, metadata, and note footers updated. Build is clean at
  97 papers / 0 errors.
- **Four works converted and verified from page 1**: PSA 2025 (`L--PSA-2025`, merged Q1–Q4 HFCE
  releases), PSA 2026 (`L--PSA-2026`, merged Q1–Q2), Federal Reserve 2024 (`I--FederalReserve-2024`),
  Guo et al. 2024 (`A--Guo-2024`).
- **Provenance reconciled**: the earlier suspicion that nine metadata keys had no matching PDF
  is resolved — every `metadata.json` `source_pdf` now exists on disk (132 PDFs, no duplicates,
  none missing). The starchy cases were all filename/content misnamings already corrected in the
  sidecar: D'Souza, Dela Cruz (Cruz), El Hajj (Hajj), Sai Sanhosh R (R & Singh), Sapiri
  (Awaluddin), Hamdare (Agrawal), Zhao (R. Huang), Atento (Espelita), de Zarzà (2023-dated PDF).
- **BSP filename pairs restored**: `2023a` (9-page financial-inclusion dashboard) and `2023b`
  (69-page RREDP), and `2026a` (24-page CES Q2 2026) and `2026b` (72-page Q1 2026 REDF), had been
  swapped on disk; files and `metadata.json` `source_pdf` are now consistent (see the entries'
  `FILENAME RECONCILED 2026-10-08` notes).
- **Duplicate PDFs removed**: `Bangko Sentral ng Pilipinas, 2025b.pdf` (copy of 2025.pdf),
  `n.d.(a).pdf` (copy of 2026c.pdf), `n.d.(b).pdf` (copy of 2019.pdf),
  `de Zarza et al., 2023.pdf` (copy of `De Zarzà et al., 2023.pdf`), and
  `Philippine Statistics Authority, 2025.pdf` (copy of 2025d.pdf).
- **Left as-is**: four stale `.html` intake pages in `paper-pdfs/` (Metrobank 2022, RCBC 2024,
  Financial Planning Association, Tamplin 2024) are uncited and unconverted and are not part of
  any citation resolution.

---

## What changed since `NEW-SCOPE-SOURCES.md` P0.4 (2026-09-27)

| Old six-unheld item | Status now |
| :--- | :--- |
| Brooke (1996) | Still cited, still unheld |
| PSA (2023) FIES | **No longer cited** in V4; replaced by PSA 2025 and PSA 2026, now held (`L--PSA-2025`, `L--PSA-2026`) |
| PSA (2026) HFCE | **Now held** (`L--PSA-2026`, converted 2026-10-08) |
| Ariningsih & Muhammad (2024) | Still cited, still unheld |
| Lianto et al. (2023) | Still cited, still unheld |
| Lim et al. (2025) | Still cited, still unheld |

Dasmariñas (2024), the old P0.1 gap, is now held and well cited. Two previously-tracked P1
items are addressed here: `A--DeyArefin-2025` (rule-based household budget) is now held, and
Guo et al. (2024) is now held as `A--Guo-2024` (BVA test-case generation, cited in Chapter 2 —
converted 2026-10-08).

---

## Recommended acquisition order

The P0.4 top priority (PSA HFCE) and the four converted works (PSA 2025, PSA 2026, Board of
Governors 2024, Guo et al. 2024) are **now held**. The remaining 25 unheld works, in order:

1. **BSP (2024a-d) Consumer Expectations Survey reports** — four quarterlies cited in Chapter 1 for
   saving-rate and household-buffer claims; official releases, cheap to fetch as a set.
2. **Rule-based-classification cluster (now minus the held Federal Reserve report)** — Bhutta et al.
   (2023), Adams et al. (2022), He and Zhou (2022), Tukey (1977). Cited by **both** Chapters 2
   and 3; these give Chapter 3's boundaries their evidence. `A--DeyArefin-2025` is already held
   as the in-corpus precedent.
3. **In-window official-body and finance singles** — FSCC (2024), Simonse et al. (2024),
   Hamid et al. (2023), Bunyi (2024), Laaber et al. (2024), Sathe and Panse (2023).
4. **Evaluation cluster (P0.3)** — Ariningsih & Muhammad (2024), Lianto et al. (2023), Lim et
   al. (2025), plus Brooke (1996) as the one-page window exception.
5. **Canonical-method singles** — Box and Jenkins (1970), Dantzig (1963), Bangor et al. (2008),
   Lewis (2018), Hyndman and Kostenko (2007). Decide the window extension first (see the
   cross-cutting finding above and the updated window ruling in `NEW-SCOPE-SOURCES.md`); these
   are the canonical/instrument works now citable under the extended exception.
6. **Standard** — ISO/IEC 25010 (2023), cited in Chapter 2, admissible without a corpus file
   under the standard exception.

A 25-row decision matrix for these works is recorded in `docs/NEW-SCOPE-SOURCES.md`.