# Batch-6 Algorithm/Model Screening (Budi Intake)

Screening of `Odin-Paper/archived-literature/papers/batch-6/` for papers discussing
**models and algorithms used to improve a user's personal savings and debt** in
intelligent personalized finance management systems.

- **Date:** 2026.09.05
- **Source:** `Odin-Paper/archived-literature/papers/batch-6/` (14 PDFs, newest intake)
- **Primary filter:** `Odin-Literature/scores/index.json` (old 518-paper run) + `scores/report.md`
- **Reference outline:** `Odin-Paper/google-drive/topical-outline/topical-outline.md` (System Models and Algorithms, §3)
- **Status:** screening only — no PDFs copied, converted, summarized, or scored yet

---

## Method

1. Enumerate all 14 PDFs in `batch-6/`.
2. Pull per-paper module scores, best module, tier, and quality from `scores/index.json`
   (the old-run scores; titles/designation for batch-6 were missing there, so titles were
   recovered directly from PDF metadata / first page).
3. Classify each paper against the Budi modules in `config/modules.yaml`, focused on the
   algorithm/model modules: `ml_algorithms`, `forecasting`, `anomaly_detection`,
   `budget_recommendation`, `expense_categorization`, `savings`, `debt_management`.
4. Verdict per paper: **Maintain** (recommend intake), **Review** (borderline / partial fit),
   or **Cull / Defer** (low relevance or off-scope).

Tier thresholds: crucial >= 0.45, supporting >= 0.30, cull < 0.30 (per `config/modules.yaml`).

---

## Batch-6 Triage

| Proposed stem | Full title | Year | Source PDF | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :--- | :---: | :---: |
| `A--Zhong-2025` | Adaptive Anomaly Detection Threshold for Financial Data Quality Monitoring Based on Time Series Features | 2025 | `Zhong.pdf` | anomaly_detection 0.522 | crucial / 1.25 | **Maintain** |
| `A--Zlobin-2025` | Systematic Review of Deep and Machine Learning for Financial Modeling | 2025 | `Zlobin & Bazylevych.pdf` | ml_algorithms 0.509 | crucial / 1.25 | **Maintain** |
| `A--ZhangDuan-2025` | Accounting Data Anomaly Detection and Prediction Based on Self-Supervised Learning | 2025 | `Zhang & Duan.pdf` | anomaly_detection 0.478 | crucial / 1.50 | **Maintain** |
| `I--ZhangLu-2026` | Artificial Intelligence-Driven Transformation in Financial Technology: Applications, Agents and Challenges | 2026 | `Zhang & Lu.pdf` | ml_algorithms 0.457 | crucial / 1.50 | Maintain |
| `I--Zole-2025` | WELTH - AI Finance Platform | 2025 | `Zole & Wagh.pdf` | pfms_systems 0.463 | crucial / 1.25 | Maintain (PFM system; algorithm-light) |
| `A--ZhangEtAl-2023` | An Experimental Evaluation of Anomaly Detection in Time Series | 2023 | `Zhang et al.pdf` | anomaly_detection 0.411 | supporting / 1.25 | Maintain (methodology) |
| `I--ZhangHou-2026` | Consumer Behavior Data Mining and Analysis Using Machine Learning Algorithms | 2026 | `Zhang & Hou.pdf` | ml_algorithms 0.436 | supporting / 1.00 | Maintain (expense-category angle) |
| `I--ZhouHe-2023` | Rare Category Analysis for Complex Data: A Review | 2023 | `Zhou & He.pdf` | anomaly_detection 0.410 | supporting / 1.50 | Review |
| `I--ZhangSussman-2024` | Income Predictability and Budgeting | 2024 | `Zhang & Sussman.pdf` | financial_profile_classification 0.412 | supporting / 1.50 | Review (behavioral, no algorithm) |
| `I--Zhu-2024a` | Upgrading Financial Education by Adding Python-Based Personalized Financial Projection: A Randomized Control Trial | 2024 | `Zhu-2023.pdf` | behavioral_insights 0.450 | crucial / 1.50 | Review (behavioral, personalized) |
| `I--Zhu-2024b` | Optimizing Financial Decision-Making for Emerging Adults: A Compact Python-Based Personalized Financial Projection | 2024 | `Zhu-2024.pdf` | financial_literacy 0.412 | supporting / 1.25 | Review (behavioral, personalized) |
| `I--ZhuEtAl-2023` | Not Transparent and Incomprehensible: A Qualitative User Study of an AI-Empowered Financial Advisory System | 2023 | `Zhu et al.pdf` | system_evaluation 0.387 | supporting / 1.25 | Review (UX/acceptance) |
| `I--Zihan-2025` | FinTech Development and Its Role in Financial Inclusion: The Enabling Role of Artificial Intelligence in Digital Financial Services | 2025 | `Zihan.pdf` | pfms_systems 0.389 | supporting / 1.00 | Cull / Defer (5 pp, conceptual) |
| `I--Zhao-2026` | DynEC: Dynamic Evolutionary Clustering for Power User Load Profiling Using Multi-View Graph Neural Networks | 2026 | `Zhao et al.pdf` | synthetic_data_mlops 0.269 | cull / 1.50 | Cull (electricity load, off-scope) |

> **Stem note:** batch-6 titles/designations were absent from the old manifest, so proposed
> stems are new and must be validated against the real author lists during summarize (step 3).
> Prefixes follow `docs/standards/rrl-naming-conventions.md` (`A--` algorithm/system,
> `I--` international). Suffixes are provisional.

---

## Algorithm/Model-Designated Papers (Budi Candidates)

### Crucial tier (top priority for intake)

1. **Zhong (2025)** — *Adaptive Anomaly Detection Threshold for Financial Data Quality Monitoring Based on Time Series Features*
   - **Best module:** anomaly_detection 0.522 (crucial); ml_algorithms 0.370.
   - **Why it fits:** core overspending/anomaly detection algorithm for a PFM app — adaptive,
     time-series thresholds for anomalous spending/financial data quality. Directly supports
     topical outline §3 (models & algorithms) and module `anomaly_detection`.
   - **Source:** `Odin-Paper/archived-literature/papers/batch-6/Zhong.pdf` (10 pp).

2. **Zlobin & Bazylevych (2025)** — *Systematic Review of Deep and Machine Learning for Financial Modeling*
   - **Best module:** ml_algorithms 0.509 (crucial); forecasting 0.390, anomaly_detection 0.367.
   - **Why it fits:** comprehensive ML/DL-for-finance survey (classification & regression) —
      41 papers analyzed. Strong foundation for the algorithm selection section §3.
   - **Source:** `Zlobin & Bazylevych.pdf` (12 pp). Ukrainian; survey-based.

3. **Zhang & Duan (2025)** — *Accounting Data Anomaly Detection and Prediction Based on Self-Supervised Learning*
   - **Best module:** anomaly_detection 0.478 (crucial); forecasting 0.339, ml_algorithms 0.416.
   - **Why it fits:** self-supervised framework (HFSL) for anomaly detection + prediction on
      accounting/financial data — a models-and-algorithms paper for spending anomaly detection.
   - **Source:** `Zhang & Duan.pdf` (25 pp).

### Supporting tier (promising, needs RRL verdict)

4. **Zhang et al. (2023)** — *An Experimental Evaluation of Anomaly Detection in Time Series* (PVLDB)
   - **Best module:** anomaly_detection 0.411 (supporting).
   - **Why it fits:** benchmarks 17 anomaly-detection algorithms with taxonomy — useful as a
     baseline/comparison section in §3. Not finance-specific but methodologically strong.
   - **Source:** `Zhang et al.pdf` (14 pp).

5. **Zhang & Hou (2026)** — *Consumer Behavior Data Mining and Analysis Using Machine Learning Algorithms*
   - **Best module:** ml_algorithms 0.436 (supporting); expense_categorization 0.326.
   - **Why it fits:** compares LR/SVM/RF/XGBoost on consumer behavior, relevant to expense
      categorization and classification-based features. Broad behavioral, not strictly savings/debt.
   - **Source:** `Zhang & Hou.pdf` (6 pp).

6. **Zhang & Lu (2026)** — *AI-Driven Transformation in Financial Technology: Applications, Agents and Challenges* (review)
   - **Best module:** ml_algorithms 0.457 (crucial); pfms 0.354, privacy 0.366, debt 0.329, etc.
   - **Why it fits:** wide AI-in-fintech review; relevant to intelligent PFM features (§2.4).
      Breadth over depth — treat as context, not as the algorithm core.
   - **Source:** `Zhang & Lu.pdf` (36 pp).

### Review / borderline (person/behavior oriented — not primary algorithm papers)

7. **Zhang & Sussman (2024)** — *Income Predictability and Budgeting*
   - **Best module:** financial_profile_classification 0.412 (supporting); budget 0.331, wellbeing 0.398.
   - **Fit:** budgeting with irregular income — the person/behavior pillar (§1.5.1 income) rather
      than algorithm. Keep only if the income-volatility/budget angle is argued.
8. **Zhu (2024a)** — *Python-Based Personalized Financial Projection... RCT* — behavioral/savings RCT,
   not an algorithm paper; supports savings & financial education (§4.3/§4.4) contextually.
9. **Zhu (2024b)** — *Optimizing Financial Decision-Making for Emerging Adults...* — same pair; literacy +
   savings + behavior. No ML; personalized projection tooling.
10. **Zhu et al. (2023)** — *Robo-advisor UX study* — system_evaluation/TAM angle; supports §5
    (acceptance) and robo-advisor features (§2.4.4.2), not algorithms.
11. **Zhou & He (2023)** — *Rare Category Analysis for Complex Data: A Review* — anomaly/rare-category
    review used for fraud/network; tangential to savings/debt PFM. Methodology reference only.

### Cull / defer

12. **Zihan (2025)** — *FinTech Development and Financial Inclusion* — 5-page conceptual conference
    paper; strong keywords ("AI", "digital financial services") but no model/algorithm content.
13. **Zhao et al. (2026)** — *DynEC... Power User Load Profiling (GNN)* — electricity load profiling;
    best score 0.269 (cull), off-scope for personal savings/debt finance.

---

## Topical Outline Mapping ($3 System Models and Algorithms)

| Paper | Topical outline node | Notes |
| :--- | :--- | :--- |
| Zhong 2025 | §3.1/§3.3 (datasets, algorithms), anomaly detection | Adaptive time-series thresholding |
| Zlobin & Bazylevych 2025 | §3.2/§3.3 (models & algorithms), ML/DL survey | Direct §3 foundation |
| Zhang & Duan 2025 | §3.2/§3.3, anomaly + forecasting | Self-supervised accounting anomaly |
| Zhang et al 2023 | §3.2 anomaly methods | Benchmark/taxonomy |
| Zhang & Hou 2026 | §2.4.4.1 / §3 classification | ML classifier comparison |
| Zhang & Lu 2026 | §2.4.1 (AI features), PFM architecture | Broad fintech-AI context |

The remaining papers map mostly to §1 (person/behavior), §2.2 (PFM types), and §5 (evaluation),
which are outside the algorithm/model focus requested here.

---

## Recommended Next Steps

1. **Confirm verdicts** for the three "Review" algorithm papers (Zhang & Sussman, Zhu pair,
   Zhou & He) — researcher decision.
2. **Intake the Maintain set** per `docs/standards/rrl-workflow.md` (batch-7 runbook):
   copy to `literature/bucket/` → `fetch_pdfs.py` → `prepare_pdf.py` → rename with the
   canonical stems above → summarize `_summarized.json` → `embed.py` + `score.py`.
3. **Proceed to batch-5 screening** next (alphabetical previous batch), repeating this method.
4. **Re-score** once conversions land — these old-run scores (0.478/0.522 etc.) were computed
   from the deprecated 518-paper corpus and will be replaced by the batch-7 run.