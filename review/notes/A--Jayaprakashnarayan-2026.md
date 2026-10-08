---
paper_id: A--Jayaprakashnarayan-2026
first_author: Jayaprakashnarayan
year: 2026
title: "AI-Enabled NLP Framework for Automated Expense Management and Financial Analysis"
venue: "International Journal of Engineering & Extended Technologies Research (IJEETR)"
doi: 10.15662/IJEETR.2026.0802073
designation: algorithm
status: extracted
modules: [income_expense_management, budgeting, pfm_apps_features, pfm_apps_importance, pfm_apps_problems, rule_based_classification, model_algorithm_integration, data_collection, model_development, system_development, model_performance_evaluation, system_performance_evaluation, software_quality_evaluation]
module_rationale:
  income_expense_management: "The framework's stated purpose is automated tracking, categorization and analysis of personal financial transactions from SMS and notifications (Abstract, p. 1138; Sect. III.A, p. 1144)."
  budgeting: "The system provides budget utilization review and an Algorithm 1 step 'check_budget_limits(transaction)' after each recorded transaction (Abstract, p. 1138; Algorithm 1, p. 1151)."
  pfm_apps_features: "Named feature set includes interactive dashboards for spending patterns, budget utilization, financial goals, alerts and uncertainty flags (Abstract, p. 1138; Sect. III.A, p. 1145)."
  pfm_apps_importance: "The paper claims the approach 'reduces manual effort by 85.6% while improving financial awareness through actionable intelligence' (Abstract, p. 1138)."
  pfm_apps_problems: "The introduction describes a fragmented financial landscape and states existing apps support only major banks and English-language messages (Sect. I, p. 1138; Sect. I.A, p. 1139)."
  rule_based_classification: "Rule-based screening is one of three ensemble fraud detectors, and rule-based baselines are benchmarked for entity extraction (Table I, p. 1153; Sect. III.E, p. 1149)."
  model_algorithm_integration: "The framework is explicitly a unified multi-task architecture combining transformer encoders, multi-task heads, an ensemble anomaly detector and an adaptive personalization layer (Sect. III.A, p. 1144)."
  data_collection: "Two-phase dataset construction is described in detail: a curated 124,583-message Phase 1 set and a 187,342-transaction Phase 2 deployment set (Sect. III.B, p. 1145; Tables I-II, p. 1146)."
  model_development: "Encoder fine-tuning, multi-task loss weighting, augmentation strategy and uncertainty thresholding are specified (Sect. III.C-III.D, pp. 1147-1148)."
  system_development: "Implementation stack is stated: PyTorch 2.0, TensorFlow Lite conversion, 8-bit quantization and pruning for on-device deployment (Sect. IV.A, p. 1152; Sect. III.F, p. 1150)."
  model_performance_evaluation: "Component-level evaluation reports precision, recall, F1 and accuracy for entity extraction, classification and fraud detection (Sect. IV.B-IV.D, pp. 1153-1156)."
  system_performance_evaluation: "Latency, memory, battery impact and the Phase 2 longitudinal deployment are reported as system-level measures (Sect. IV.A, p. 1152; Sect. VI.B, p. 1158)."
  software_quality_evaluation: "Phase 4 of the evaluation strategy names the System Usability Scale as the usability instrument (Sect. I.E, p. 1141)."
---

## Summary

The paper proposes an on-device AI-enabled Natural Language Processing framework that reads financial SMS alerts and mobile notifications, extracts transaction entities (amount, date, time, merchant, account, transaction type), classifies each transaction into one of 14 expense categories, screens for fraud, and presents spending insights through dashboards. The architecture has four stated components: a transformer encoder initialized from MuRIL and fine-tuned on a financial SMS corpus; a multi-task learning head that performs token-level entity extraction and sequence-level classification simultaneously over shared representations; an ensemble fraud detector combining rule-based screening, Isolation Forest statistical anomaly detection and an LSTM autoencoder; and an adaptive personalization layer that updates models on-device from user corrections. Uncertainty is modeled explicitly at token and sequence level, with low-confidence items routed to human review rather than auto-committed. Evaluation is described as two-phase: a curated Phase 1 dataset of 124,583 financial SMS messages from 250 volunteer participants in India, and a Phase 2 six-month deployment with 50 participants generating 187,342 transactions. Reported results include an entity-extraction F1 of 0.968 for the proposed model against 0.940 for fine-tuned FinBERT and 0.888 for BiLSTM-CRF, a weighted-average classification F1 of 0.949, and an ensemble fraud detector with 0.917 sensitivity at 0.038 false positive rate. Section V then restates the framework's performance as *expected* rather than measured, and the conclusion's false-positive figure (4.1%) does not match the results section (0.038). The paper also contains an unannounced switch to a different framework name ("SENA-GR") at the start of the fraud-detection results, and the reference list is partly composed of unrelated power-electronics citations.

## Problem and Motivation

Digital payment adoption has generated a volume of transactional notifications that exceeds what individuals can track manually. The introduction states that "the average smartphone user now receives dozens of financial notifications daily across multiple bank accounts, credit cards, UPI applications, and digital wallets, creating a fragmented financial landscape that defies easy comprehension and control" (Sect. I, p. 1138). The paper attributes this to a paradox: the shift to cashless economies should simplify finance but has made personal financial management more complex.

The authors frame the central technical problem as extracting structured intelligence from unstructured financial communications. The system must interpret diverse message formats, handle code-mixed languages, identify merchant entities despite inconsistent naming, categorize transactions, detect anomalies and present insights — all within mobile privacy and compute constraints (Sect. I, p. 1138). Two existing approach families are rejected. Rule-based systems require manual pattern maintenance for each message format and break when a bank edits its SMS template; the paper notes that a typical Indian banking ecosystem involves "over 200 banks, dozens of UPI applications, and countless variations in message formatting across regions and languages" (Sect. I, p. 1139). Supervised learning approaches are described as assuming static deployment environments and unable to evolve as formats change or new fraud patterns emerge.

A second motivation is linguistic. The paper argues that financial SMS in India frequently mixes English numerals with Hindi script and Hinglish colloquialisms, and that rule-based systems struggle with this variability while supervised models need annotated data per language combination. The consequence, per the authors, is that "existing financial management applications often provide incomplete coverage, supporting only major banks and English-language messages while leaving users from diverse linguistic backgrounds underserved" (Sect. I.A, p. 1139). The stated corrective is a framework that treats financial language understanding as a dynamic, continuously adapting capability rather than a fixed artifact, with on-device personalization so raw messages never leave the phone.

## Method

**Design.** No formal design label is stated. The paper is a framework-development study that combines component-level benchmark evaluation on a curated corpus (Sect. IV, pp. 1152-1156), a longitudinal deployment study (Sect. III.B, p. 1146), and a section explicitly headed "Expected Results and Discussion" that presents projections rather than measurements (Sect. V, p. 1156).
**Sample.** Phase 1: N = 124,583 financial SMS messages, unit of analysis = one SMS message, drawn from 250 volunteer participants and 347 unique sender IDs; Phase 2: N = 187,342 transactions processed, unit of analysis = one transaction, from 50 participants over 6 months.
**Context.** geography: India — participants drawn from urban (65%) and semi-urban (35%) locations, with messages from 42 Indian banks, 18 UPI applications, 23 credit card providers and 14 digital wallet services (Sect. III.B, p. 1146); population: smartphone users receiving financial notifications — students (18%), working professionals (52%), business owners (15%) and retirees (15%) (Sect. III.B, p. 1145); setting: on-device Android processing across three device tiers (2GB/Snapdragon 400, 4GB/Snapdragon 600, 8GB/Snapdragon 800), with model training performed offline on NVIDIA Tesla V100 GPUs using PyTorch 2.0 and deployment via TensorFlow Lite (Sect. IV.A, p. 1152).

The framework's processing pipeline is stated as follows. Raw messages are first segmented to strip promotional text and disclaimers, using a rule-based algorithm keyed to financial keywords, numerical patterns and typical message structure (Sect. III.C, p. 1147). Tokenization uses the SentencePiece tokenizer from MuRIL with a maximum sequence length of 256 tokens, stated as sufficient for over 99% of the corpus (Sect. III.C, p. 1148). Training data is augmented by synonym substitution, abbreviation variation, format perturbation and code-mix injection, with all augmentations validated to preserve amount, date, merchant and transaction type (Sect. III.C, p. 1148).

The encoder is a 12-layer transformer with 768 hidden dimensions and 12 attention heads, initialized from MuRIL, pre-trained on 17 Indian languages and their code-mixed variants, then fine-tuned on the annotated financial corpus using masked language modeling and next-sentence prediction (Sect. III.D, p. 1148). The classification head applies attention pooling, then two hidden layers of 512 and 256 dimensions with ReLU activation and dropout of 0.3, before a softmax over the 14 categories (Sect. III.D, p. 1148). The combined loss weights entity and classification objectives with λ_entity = 0.7 and λ_class = 0.3 initially, adjusted dynamically on validation performance (Sect. III.D, p. 1148).

Uncertainty quantification computes token-level entropy over the tag distribution and a margin between the top two class probabilities; items exceeding thresholds are flagged for human review rather than auto-processed (Sect. III.D, pp. 1148-1149). The verification module performs fuzzy account matching (exact, partial last-4-to-6-digits, and institutional pattern matching), duplicate detection by transaction fingerprint, reference number and semantic similarity, and ensemble fraud detection over rule-based screening, an Isolation Forest trained per user, and an LSTM autoencoder (Sect. III.E, p. 1149). Model updates from user corrections occur entirely on-device; any federated contributions are encrypted, anonymized, differentially private and securely aggregated (Sect. III.F, p. 1150). Algorithm 1 gives a nine-stage processing loop from message acquisition through analytics update and notification (Algorithm 1, p. 1151).

## Software

- PyTorch 2.0 (Sect. IV.A, p. 1152)
- TensorFlow Lite (conversion target for on-device deployment) (Sect. IV.A, p. 1152)
- NVIDIA Tesla V100 GPUs (training hardware) (Sect. IV.A, p. 1152)
- MuRIL base transformer, 12 layers, 768 hidden dimensions, 12 attention heads (Sect. III.D, p. 1148)
- SentencePiece tokenizer from MuRIL; maximum sequence length 256 tokens (Sect. III.C, p. 1148)
- Isolation Forest (statistical anomaly detection component) (Sect. III.E, p. 1150)
- LSTM autoencoder (sequence anomaly detection component) (Sect. III.E, p. 1150)
- 8-bit integer quantization; pruning removing 34% of connections (Sect. III.F, p. 1150; Sect. VI.B, p. 1158)
- Custom web annotation tool for the 12-annotator labeling effort (Sect. III.B, p. 1146)
- Versions of the Isolation Forest, LSTM autoencoder and annotation tool are Not reported.

## Key Findings

- The abstract reports 96.8% accuracy in transaction extraction and 94.3% precision in merchant identification for the hybrid transformer-plus-rule architecture (Abstract, p. 1138).
- The abstract reports 91.7% sensitivity for flagging suspicious transactions with the multi-layered security protocol (Abstract, p. 1138).
- The abstract reports an 85.6% reduction in manual effort (Abstract, p. 1138).
- Entity extraction: the proposed MuRIL + multi-task model reaches 0.971 precision, 0.965 recall, 0.968 F1 and 0.964 accuracy, against 0.940 F1 for fine-tuned FinBERT, 0.888 for BiLSTM-CRF, 0.827 for CRF-only and 0.746 for the rule-based baseline (Table I, p. 1153).
- The rule-based entity extractor runs at 0.8 ms per message but its accuracy on training data (89%) drops to 61% when applied to new message formats (Sect. IV.B.1, p. 1153).
- FinBERT's F1 falls to 0.912 on code-mixed Hinglish messages versus 0.952 on English-only messages (Sect. IV.B.1, p. 1153).
- Multi-task learning adds a reported 1.2% improvement over single-task MuRIL fine-tuning (Sect. IV.B.1, p. 1153).
- By entity type, macro-average F1 is 0.966; Amount (0.988) and Date (0.983) are the easiest, Merchant (0.952) the hardest of the six typed entities (Table II, p. 1154).
- Reference numbers and UPI IDs show slightly lower performance (F1 ≈ 0.945) (Sect. IV.B.2, p. 1154).
- Transaction classification reaches a weighted-average F1 of 0.949 across 14 categories, with Income highest at F1 = 0.986 and Others lowest at F1 = 0.882 (Sect. IV.C, p. 1154; Table IV, p. 1154).
- The paper states in prose that Shopping is the greatest classification challenge (F1 = 0.924), while Table IV prints Shopping at F1 = 0.969 and Utilities at F1 = 0.924; the prose also states Utilities achieves F1 > 0.965 (Table IV, p. 1154; Sect. IV.C, p. 1154).
- Fraud detection: the rule-based detector achieves TPR = 0.673 at precision 0.482; Isolation Forest reaches 0.814 sensitivity at precision 0.563; the LSTM autoencoder reaches 0.892 sensitivity at 0.071 false positive rate; the ensemble reaches 0.917 sensitivity, 0.684 precision and 0.038 false positive rate (Sect. IV.D, pp. 1155-1156).
- The ensemble's AUC is reported as 0.956 (Sect. IV.D, p. 1156).
- The conclusion states the ensemble achieves "91.7% sensitivity with 4.1% false positive rate", which contradicts the 0.038 figure in the results section (Sect. VII, p. 1158).
- The Phase 2 study detected 23 bank format changes, 1,847 new merchant appearances, 3,421 user corrections and 17 confirmed fraud reports over six months (Table II, p. 1146).
- Quantization gives a 4× size reduction at 98.7% accuracy preservation, leaving a 1.3% accuracy loss; pruning removes 34% of connections (Sect. VI.B, p. 1158).
- Reported on-device latency is 43-127 ms, and battery impact is 0.9-2.0%/hr, rising to a projected 5-6% daily drain for users processing 300+ transactions daily (Sect. VI.B, p. 1158; Sect. VII, p. 1158).
- Section V is explicitly anticipatory: "While comprehensive empirical validation is ongoing, we project expected performance across key dimensions" (Sect. V, p. 1156), and gives expected merchant F1 = 0.948, expected Shopping F1 = 0.920, expected Others F1 = 0.876 and an expected overall F1 of 0.947.
- A direct comparison with Expensify on the test dataset is reported at 0.863 accuracy, dropping to 0.792 on Hinglish messages (Sect. V.B, p. 1157).

## Key Figures and Tables

- Table I (Phase 1 dataset, p. 1146): 124,583 messages, 250 participants, 347 sender IDs, 42 banks, 18 UPI apps, 23 credit card providers, 14 digital wallets, 37.2% code-mixed, 142-character average length, transaction types Debit 68% / Credit 24% / Refund 5% / Other 3%.
- Table II (Phase 2 longitudinal study, p. 1146): 50 participants, 6 months, 187,342 transactions, 62.4 transactions per participant per month, 23 bank format changes, 1,847 new merchants, 3,421 user corrections, 17 confirmed fraud reports.
- Table I (entity extraction benchmark, p. 1153): rule-based, CRF-only, BiLSTM-CRF, FinBERT and proposed model compared on precision, recall, F1 and accuracy — the paper reuses the "Table I" label for both the dataset summary and this results table.
- Table II (entity-level performance by type, p. 1154): Amount, Date, Time, Merchant, Account and Transaction Type with precision, recall, F1 and support, plus a macro average row.
- Table IV (transaction classification by category, p. 1154): 14-category precision/recall/F1/support breakdown; there is no Table III anywhere in the paper.
- Fig. 1 (p. 1152): Entity extraction performance comparison.
- Fig. 2 (p. 1153): Entity-level performance by type.
- Fig. 3 (p. 1154): Transaction classification performance by category.
- Fig. 4 (p. 1155): Fraud detection performance comparison.
- Fig. 5 (p. 1156): ROC curve.
- The reference list contains eleven entries labelled "Fig. 1" through "Fig. 11" that are power-electronics papers by Nagarajan, Madheswaran and others, unrelated to this paper's topic (References, pp. 1159-1160).

## Limitations and Gaps

- The results and the projections are not separated cleanly. Section IV reports component results in the past tense, while Section V is titled "Expected Results and Discussion" and states "While comprehensive empirical validation is ongoing, we project expected performance across key dimensions" (Sect. V, p. 1156). The status of the reported numbers — measured or projected — is therefore ambiguous for every figure carried in the abstract.
- The abstract's headline numbers (96.8% extraction accuracy, 94.3% merchant precision, 91.7% fraud sensitivity, 85.6% manual-effort reduction) are not reconciled with the body's F1-based tables, which report 0.968 F1 for extraction (Table I, p. 1153) and 0.917 sensitivity for fraud (Sect. IV.D, p. 1156). Neither the metric identity nor the sample on which the abstract figures rest is stated.
- The false positive rate for the fraud ensemble is 0.038 in the results section (Sect. IV.D, p. 1156) and 4.1% in the conclusion (Sect. VII, p. 1158). Both are retained here; the paper does not reconcile them.
- Shopping's F1 is printed as 0.969 in Table IV (p. 1154) while the prose says Shopping has an F1 of 0.924 and is "the greatest classification challenge"; Utilities is printed as 0.924 in Table IV while the prose says Utilities achieves F1 > 0.965. The Table IV support column also repeats 14,563 for both Shopping and Utilities.
- [unacknowledged] Section IV.D opens by describing the evaluation of "the Self-Evolving Neural Architectures using Genetic Reinforcement (SENA-GR) framework" (p. 1155), a framework name that appears nowhere else in the paper and is not the proposed framework. This is not flagged by the authors and indicates text carried over from another source.
- [unacknowledged] The reference list is partly unrelated to the paper: entries labelled Fig. 1 to Fig. 11 are power-electronics articles on resonant converters and BLDC machines (References, pp. 1159-1160). Reference numbers [12], [13] and [15] are cited in text but not listed, and [9] and [11] appear both in the figure block and in the numbered list.
- [unacknowledged] No confidence interval, p-value, standard deviation, per-fold variance or significance test is reported anywhere. Every comparative claim in Table I, Table II and Table IV is a point estimate.
- [unacknowledged] The classification evaluation reports seven of fourteen categories in Table IV; Education, Housing, Investments, Transfers, Bill Payments and Others are absent from the table (Others is discussed only in prose at F1 = 0.882).
- [unacknowledged] Table IV's own F1 column is internally inconsistent — Grocery prints 0.965/0.951/0.945, where the printed F1 (0.945) is below the printed recall (0.951), which cannot hold for a harmonic mean of the printed precision and recall.
- [unacknowledged] The 124,583-message dataset and 187,342-transaction Phase 2 dataset are both collected by the authors, but the paper states "All data collection was conducted in accordance with ethical guidelines" while the approving body is left as "the Institutional Review Board of [Institution Name]" (Sect. III.B, p. 1147) — an unfilled placeholder.
- [unacknowledged] The Phase 2 evaluation is described as partitioned "by time (first 4 months training, last 2 months evaluation)" (Sect. IV.A, p. 1152), but Phase 2 is also described as the deployment in which on-device online learning is exercised; training on the first four months of the same participants' data while evaluating on their last two months is not distinguished from the on-device adaptation effect it is meant to measure.
- [unacknowledged] No per-language result is reported for the eight languages the dataset is said to contain, apart from the FinBERT English-versus-Hinglish comparison (0.952 vs 0.912) in Sect. IV.B.1, p. 1153.
- [unacknowledged] The battery figures (0.9-2.0%/hr, 5-6% daily drain at 300+ transactions) are stated as "projected" and "while projected" (Sect. VI.B, p. 1158), so they are not measured system outcomes.
- The authors acknowledge geographic generalizability limits: the dataset is Indian, message formats differ across regions, and UPI specialization "may not transfer to ecosystems dominated by credit cards (United States), wire transfers (Europe), or mobile money (Africa)" (Sect. VI.A, p. 1157).
- The authors acknowledge that MuRIL's 17 Indian languages do not extend to Romance, Germanic or Sino-Tibetan families without substantial additional pre-training (Sect. VI.A, p. 1157).
- The authors acknowledge that on-device constraints preclude larger transformer models and that "some performance gains achievable in cloud settings are forfeited" (Sect. VI.B, p. 1157).
- The authors acknowledge that memory contention on 2GB-RAM devices "may cause the operating system to terminate background processes, reducing transaction capture rates" (Sect. VI.B, p. 1158).
- The authors acknowledge that determining optimal pruning strategies "without task-specific validation remains challenging" (Sect. VI.B, p. 1158).
- The System Usability Scale is named as a Phase 4 instrument (Sect. I.E, p. 1141) but no usability result is reported anywhere in the paper.

## Definitions

- **MuRIL** — Multilingual Representations for Indian Languages; a BERT-based model pre-trained on 17 Indian languages and their code-mixed variants, used to initialize the framework's encoder (Sect. III.A, p. 1145).
- **Multi-task learning architecture** — a shared encoder with task-specific output heads that learn entity extraction and transaction classification simultaneously from the same representations (Sect. III.A, p. 1145).
- **Uncertainty-aware processing** — explicit modeling of prediction uncertainty at token and sequence level, with low-confidence items routed to human review (Sect. III.D, pp. 1148-1149).
- **Rule-based screening** — interpretable rules for known fraud patterns, e.g. amount above ₹50,000, unusual location, unusual hour, multiple transactions to the same merchant in a short period, and velocity checks (Sect. III.E, p. 1150).
- **Isolation Forest** — a statistical anomaly detector trained on the user's historical transactions; transactions needing fewer isolation tree partitions to separate from the majority are considered anomalous (Sect. III.E, p. 1150).
- **LSTM autoencoder** — a sequence model that learns to reconstruct normal transaction sequences; high reconstruction error flags potential fraud (Sect. II.D, p. 1143; Sect. IV.D, p. 1155).
- **Transaction fingerprint** — a hash of amount + merchant + timestamp within tolerance, used for duplicate detection (Sect. III.E, p. 1150).
- **Differential privacy** — calibrated noise added to gradient updates before federated transmission, providing guarantees against inferring individual transactions (Sect. III.F, p. 1150).
- **SENA-GR** — "Self-Evolving Neural Architectures using Genetic Reinforcement"; a framework name that appears once, at the head of Sect. IV.D (p. 1155), and is otherwise unexplained.
- **Code-mixed messages** — messages mixing languages, e.g. Hinglish; 37.2% of the Phase 1 corpus (Table I, p. 1146).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Transaction extraction, proposed hybrid architecture | accuracy | 96.8% | — | — | Abstract, p. 1138 |
| Merchant identification, proposed hybrid architecture | precision | 94.3% | — | — | Abstract, p. 1138 |
| Suspicious transaction flagging, proposed security protocol | sensitivity | 91.7% | — | — | Abstract, p. 1138 |
| Manual effort reduction, proposed framework | effort reduction | 85.6% | — | — | Abstract, p. 1138 |
| Entity extraction, rule-based baseline | precision | 0.782 | — | — | Table I, p. 1153 |
| Entity extraction, rule-based baseline | recall | 0.713 | — | — | Table I, p. 1153 |
| Entity extraction, rule-based baseline | F1-score | 0.746 | — | — | Table I, p. 1153 |
| Entity extraction, rule-based baseline | accuracy | 0.724 | — | — | Table I, p. 1153 |
| Entity extraction, CRF-only baseline | precision | 0.834 | — | — | Table I, p. 1153 |
| Entity extraction, CRF-only baseline | recall | 0.821 | — | — | Table I, p. 1153 |
| Entity extraction, CRF-only baseline | F1-score | 0.827 | — | — | Table I, p. 1153 |
| Entity extraction, CRF-only baseline | accuracy | 0.819 | — | — | Table I, p. 1153 |
| Entity extraction, BiLSTM-CRF baseline | precision | 0.892 | — | — | Table I, p. 1153 |
| Entity extraction, BiLSTM-CRF baseline | recall | 0.885 | — | — | Table I, p. 1153 |
| Entity extraction, BiLSTM-CRF baseline | F1-score | 0.888 | — | — | Table I, p. 1153 |
| Entity extraction, BiLSTM-CRF baseline | accuracy | 0.881 | — | — | Table I, p. 1153 |
| Entity extraction, FinBERT fine-tuned baseline | precision | 0.943 | — | — | Table I, p. 1153 |
| Entity extraction, FinBERT fine-tuned baseline | recall | 0.938 | — | — | Table I, p. 1153 |
| Entity extraction, FinBERT fine-tuned baseline | F1-score | 0.940 | — | — | Table I, p. 1153 |
| Entity extraction, FinBERT fine-tuned baseline | accuracy | 0.936 | — | — | Table I, p. 1153 |
| Entity extraction, proposed MuRIL + multi-task | precision | 0.971 | — | — | Table I, p. 1153 |
| Entity extraction, proposed MuRIL + multi-task | recall | 0.965 | — | — | Table I, p. 1153 |
| Entity extraction, proposed MuRIL + multi-task | F1-score | 0.968 | — | — | Table I, p. 1153 |
| Entity extraction, proposed MuRIL + multi-task | accuracy | 0.964 | — | — | Table I, p. 1153 |
| Rule-based entity extraction, runtime | latency per message | 0.8ms | — | — | Sect. IV.B.1, p. 1153 |
| Rule-based entity extraction on original templates | accuracy | 89% | — | — | Sect. IV.B.1, p. 1153 |
| Rule-based entity extraction on modified templates | accuracy | 61% | — | — | Sect. IV.B.1, p. 1153 |
| FinBERT fine-tuned, English-only messages | F1 | 0.952 | — | — | Sect. IV.B.1, p. 1153 |
| FinBERT fine-tuned, code-mixed Hinglish messages | F1 | 0.912 | — | — | Sect. IV.B.1, p. 1153 |
| Multi-task learning gain over single-task MuRIL fine-tuning | improvement | 1.2% | — | — | Sect. IV.B.1, p. 1153 |
| Entity extraction by type, Amount | F1-score | 0.988 | — | — | Table II, p. 1154 |
| Entity extraction by type, Amount | support | 16,234 | — | — | Table II, p. 1154 |
| Entity extraction by type, Date | F1-score | 0.983 | — | — | Table II, p. 1154 |
| Entity extraction by type, Date | support | 15,876 | — | — | Table II, p. 1154 |
| Entity extraction by type, Time | F1-score | 0.974 | — | — | Table II, p. 1154 |
| Entity extraction by type, Time | support | 4,213 | — | — | Table II, p. 1154 |
| Entity extraction by type, Merchant | F1-score | 0.952 | — | — | Table II, p. 1154 |
| Entity extraction by type, Merchant | support | 15,234 | — | — | Table II, p. 1154 |
| Entity extraction by type, Account | F1-score | 0.970 | — | — | Table II, p. 1154 |
| Entity extraction by type, Account | support | 14,987 | — | — | Table II, p. 1154 |
| Entity extraction by type, Transaction Type | F1-score | 0.959 | — | — | Table II, p. 1154 |
| Entity extraction by type, Transaction Type | support | 15,432 | — | — | Table II, p. 1154 |
| Entity extraction, Macro Average | precision | 0.969 | — | — | Table II, p. 1154 |
| Entity extraction, Macro Average | recall | 0.963 | — | — | Table II, p. 1154 |
| Entity extraction, Macro Average | F1-score | 0.966 | — | — | Table II, p. 1154 |
| Reference numbers and UPI IDs, proposed model | F1-score | 0.945 | — | — | Sect. IV.B.2, p. 1154 |
| Transaction classification, weighted average across 14 categories | F1-score | 0.949 | — | — | Sect. IV.C, p. 1154 |
| Transaction classification, Food & Dining | F1-score | 0.954 | — | — | Table IV, p. 1154 |
| Transaction classification, Grocery | F1-score | 0.945 | — | — | Table IV, p. 1154 |
| Transaction classification, Transportation | F1-score | 0.959 | — | — | Table IV, p. 1154 |
| Transaction classification, Shopping (as printed in Table IV) | F1-score | 0.969 | — | — | Table IV, p. 1154 |
| Transaction classification, Shopping (as stated in prose) | F1-score | 0.924 | — | — | Sect. IV.C, p. 1154 |
| Transaction classification, Utilities (as printed in Table IV) | F1-score | 0.924 | — | — | Table IV, p. 1154 |
| Transaction classification, Utilities (as stated in prose) | F1-score | > 0.965 | — | — | Sect. IV.C, p. 1154 |
| Transaction classification, Entertainment | F1-score | 0.969 | — | — | Table IV, p. 1154 |
| Transaction classification, Healthcare | F1-score | 0.963 | — | — | Table IV, p. 1154 |
| Transaction classification, Income | F1-score | 0.986 | — | — | Sect. IV.C, p. 1154 |
| Transaction classification, Others | F1-score | 0.882 | — | — | Sect. IV.C, p. 1154 |
| Fraud detection, rule-based detector | true positive rate | 0.673 | — | — | Sect. IV.D, p. 1155 |
| Fraud detection, rule-based detector | precision | 0.482 | — | — | Sect. IV.D, p. 1155 |
| Fraud detection, Isolation Forest | sensitivity | 0.814 | — | — | Sect. IV.D, p. 1155 |
| Fraud detection, Isolation Forest | precision | 0.563 | — | — | Sect. IV.D, p. 1155 |
| Fraud detection, LSTM autoencoder | sensitivity | 0.892 | — | — | Sect. IV.D, p. 1156 |
| Fraud detection, LSTM autoencoder | false positive rate | 0.071 | — | — | Sect. IV.D, p. 1156 |
| Fraud detection, proposed ensemble | sensitivity | 0.917 | — | — | Sect. IV.D, p. 1156 |
| Fraud detection, proposed ensemble | false positive rate | 0.038 | — | — | Sect. IV.D, p. 1156 |
| Fraud detection, proposed ensemble | precision | 0.684 | — | — | Sect. IV.D, p. 1156 |
| Fraud detection, proposed ensemble | AUC | 0.956 | — | — | Sect. IV.D, p. 1156 |
| Fraud detection, proposed ensemble (conclusion restatement) | false positive rate | 4.1% | — | — | Sect. VII, p. 1158 |
| Fraud detection, proposed ensemble (conclusion restatement) | sensitivity | 91.7% | — | — | Sect. VII, p. 1158 |
| Phase 1 dataset | total messages | 124,583 | — | — | Table I, p. 1146 |
| Phase 1 dataset | unique participants | 250 | — | — | Table I, p. 1146 |
| Phase 1 dataset | unique sender IDs | 347 | — | — | Table I, p. 1146 |
| Phase 1 dataset | banks represented | 42 | — | — | Table I, p. 1146 |
| Phase 1 dataset | UPI apps represented | 18 | — | — | Table I, p. 1146 |
| Phase 1 dataset | credit card providers | 23 | — | — | Table I, p. 1146 |
| Phase 1 dataset | digital wallets | 14 | — | — | Table I, p. 1146 |
| Phase 1 dataset | code-mixed messages | 37.2% | — | — | Table I, p. 1146 |
| Phase 1 dataset | average message length | 142 characters | — | — | Table I, p. 1146 |
| Phase 1 dataset, transaction types | debit / credit / refund / other | Debit: 68%, Credit: 24%, Refund: 5%, Other: 3% | — | — | Table I, p. 1146 |
| Phase 1 annotation, entity boundaries | Cohen's Kappa | 0.89 | — | — | Sect. III.B, p. 1146 |
| Phase 1 annotation, entity types | Cohen's Kappa | 0.92 | — | — | Sect. III.B, p. 1146 |
| Phase 1 annotation team | annotators | 12 | — | — | Sect. III.B, p. 1146 |
| Phase 2 dataset | participants | 50 | — | — | Table II, p. 1146 |
| Phase 2 dataset | duration | 6 months | — | — | Table II, p. 1146 |
| Phase 2 dataset | total transactions processed | 187,342 | — | — | Table II, p. 1146 |
| Phase 2 dataset | average transactions per participant per month | 62.4 | — | — | Table II, p. 1146 |
| Phase 2 dataset | bank format changes detected | 23 | — | — | Table II, p. 1146 |
| Phase 2 dataset | new merchant appearances | 1,847 | — | — | Table II, p. 1146 |
| Phase 2 dataset | user corrections provided | 3,421 | — | — | Table II, p. 1146 |
| Phase 2 dataset | confirmed fraud reports | 17 | — | — | Table II, p. 1146 |
| Dataset split, training partition | messages | 87,208 (70%) | — | — | Sect. IV.A, p. 1152 |
| Dataset split, validation partition | messages | 18,687 (15%) | — | — | Sect. IV.A, p. 1152 |
| Dataset split, test partition | messages | 18,688 (15%) | — | — | Sect. IV.A, p. 1152 |
| Preliminary experiment used for projected results | messages | 15,000 | — | — | Sect. V.A, p. 1157 |
| Projected entity extraction, Merchant | F1-score | 0.948 | — | — | Sect. V.A, p. 1157 |
| Projected entity extraction, reference numbers and UPI IDs | F1-score | 0.94 | — | — | Sect. V.A, p. 1157 |
| Projected transaction classification, Shopping | F1-score | 0.920 | — | — | Sect. V.B, p. 1157 |
| Projected transaction classification, Others | F1-score | 0.876 | — | — | Sect. V.B, p. 1157 |
| Projected overall transaction classification | F1-score | 0.947 | — | — | Sect. V.B, p. 1157 |
| Commercial expense application comparison, Expensify | accuracy | 0.863 | — | — | Sect. V.B, p. 1157 |
| Commercial expense application comparison, Expensify on Hinglish | accuracy | 0.792 | — | — | Sect. V.B, p. 1157 |
| On-device model size across device classes | size | 124-183MB | — | — | Sect. VI.B, p. 1157 |
| Quantization | size reduction | 4× | — | — | Sect. VI.B, p. 1158 |
| Quantization | accuracy preservation | 98.7% | — | — | Sect. VI.B, p. 1158 |
| Quantization | remaining accuracy loss | 1.3% | — | — | Sect. VI.B, p. 1158 |
| Pruning | connections removed | 34% | — | — | Sect. VI.B, p. 1158 |
| On-device processing | latency | 43-127ms | — | — | Sect. VII, p. 1158 |
| On-device battery impact | battery drain per hour | 0.9-2.0%/hr | — | — | Sect. VI.B, p. 1158 |
| On-device battery impact at 300+ daily transactions | daily battery drain | 5-6% | — | — | Sect. VI.B, p. 1158 |
| Prior work, Kumar et al. rule-based bank SMS extraction | accuracy | 89% | — | — | Sect. II.B, p. 1142 |
| Prior work, Sharma and Gupta BiLSTM-CRF | F1-score | 92.3% | — | — | Sect. II.B, p. 1142 |
| Prior work, Sharma and Gupta dataset size | messages | 8,000 | — | — | Sect. V.A, p. 1157 |
| Prior work, Wang et al. hierarchical attention transaction classification | accuracy | 91.2% | — | — | Sect. II.C, p. 1143 |
| Prior work, Lee and Kim personalized categorization | user satisfaction | 94.7% | — | — | Sect. II.C, p. 1143 |
| Prior work, Lee and Kim non-personalized baseline | user satisfaction | 78.3% | — | — | Sect. II.C, p. 1143 |
| Prior work, Ahmed et al. LSTM autoencoder fraud detection | sensitivity | 89.2% | — | — | Sect. II.D, p. 1143 |
| Prior work, Ahmed et al. LSTM autoencoder fraud detection | false positive rate | 4.7% | — | — | Sect. II.D, p. 1143 |
| Prior work, Wang et al. graph-based fraud detection | precision improvement | 15% | — | — | Sect. II.D, p. 1143 |
| Prior work, Ahmed and Mahmood hybrid fraud system | sensitivity | 91.7% | — | — | Sect. II.D, p. 1144 |
| Prior work, Ahmed and Mahmood hybrid fraud system | false positive rate | 3.8% | — | — | Sect. II.D, p. 1144 |
| Indian banking ecosystem described in the introduction | banks | 200 | — | — | Sect. I, p. 1139 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "We introduce a novel hybrid architecture combining transformer-based language models with rule-based verification systems to achieve 96.8% accuracy in transaction extraction and 94.3% precision in merchant identification." | Abstract, p. 1138 | model_algorithm_integration |
| "The framework incorporates a multi-layered security protocol that detects fraudulent patterns and flags suspicious transactions with 91.7% sensitivity." | Abstract, p. 1138 | model_algorithm_integration |
| "Experimental evaluation using real-world transaction datasets demonstrates that our approach reduces manual effort by 85.6% while improving financial awareness through actionable intelligence." | Abstract, p. 1138 | pfm_apps_importance |
| "The average smartphone user now receives dozens of financial notifications daily across multiple bank accounts, credit cards, UPI applications, and digital wallets, creating a fragmented financial landscape that defies easy comprehension and control" | Sect. I, p. 1138 | pfm_apps_problems |
| "Automated parsing of financial SMS messages presents unique challenges distinct from general-purpose text processing. Financial alerts are characterized by extreme conciseness, domain-specific abbreviations, inconsistent formatting across institutions, and frequent code-mixing between languages" | Sect. II.B, p. 1142 | income_expense_management |
| "The proposed MuRIL-based multi-task architecture achieves superior performance across all entity types, with an overall F1-score of 0.968, significantly outperforming rule-based, CRF-only, and BiLSTM-CRF baselines." | Sect. IV.B.1, p. 1153 | model_performance_evaluation |
| "The rule-based detector, while highly interpretable and computationally efficient, misses nearly one-third of fraudulent transactions (TPR=0.673)." | Sect. IV.D, p. 1155 | rule_based_classification |
| "The proposed ensemble combines these complementary strengths through weighted voting, with weights optimized on validation data. The ensemble achieves superior sensitivity (0.917) while reducing false positives below even the rule-based detector (0.038)." | Sect. IV.D, p. 1156 | model_algorithm_integration |
| "All core NLP processing—message parsing, entity extraction, transaction classification, fraud detection—executes entirely on the user's device." | Sect. III.F, p. 1150 | system_development |
| "While on-device processing offers privacy benefits, it imposes significant computational constraints that limit model sophistication" | Sect. VI.B, p. 1157 | system_performance_evaluation |
| "The primary dataset used in this research comprises financial SMS messages from Indian banks, UPI applications, and digital payment platforms." | Sect. VI.A, p. 1157 | data_collection |
| "Rather than making binary decisions with false confidence, the system explicitly models its own uncertainty at each processing stage and adjusts its behavior accordingly." | Sect. III.A, p. 1145 | model_algorithm_integration |
| "When users correct misclassified transactions, flag false fraud alerts, or confirm suspicious transactions as legitimate, these interactions generate training signals that update the underlying models entirely on-device." | Sect. III.A, p. 1145 | model_development |
| "The longitudinal nature of Phase 2 enables unique evaluation capabilities not possible with static datasets." | Sect. III.B, p. 1146 | system_performance_evaluation |
| "While comprehensive empirical validation is ongoing, we project expected performance across key dimensions and discuss the implications of these findings for research and practice." | Sect. V, p. 1156 | model_performance_evaluation |
| "Standardized usability metrics (System Usability Scale) and qualitative feedback will capture user perceptions of the system's accuracy, helpfulness, and trustworthiness" | Sect. I.E, p. 1141 | software_quality_evaluation |
| "Transactions flagged as potential duplicates are grouped and presented to users for confirmation, with only one transaction incorporated into financial records unless user indicates multiple distinct transactions occurred." | Sect. III.E, p. 1150 | budgeting |
| "By reducing the need for manual tracking and expert financial knowledge, the framework makes sophisticated financial management accessible to populations traditionally underserved by financial technology" | Sect. I.F, p. 1141 | pfm_apps_features |

## Remember This

- The framework is an on-device NLP pipeline: MuRIL transformer encoder, multi-task entity-extraction-plus-classification head, ensemble fraud detection, and on-device personalization from user corrections.
- Phase 1 uses 124,583 Indian financial SMS messages from 250 participants; Phase 2 adds 187,342 transactions from 50 participants over six months.
- Entity extraction F1 for the proposed model is 0.968, against 0.940 for fine-tuned FinBERT, 0.888 for BiLSTM-CRF, 0.827 for CRF-only and 0.746 for rule-based.
- Transaction classification reaches a weighted-average F1 of 0.949; Table IV and the prose disagree on which category is hardest (Shopping 0.969 in the table vs 0.924 in text; Utilities 0.924 in the table vs > 0.965 in text).
- Fraud ensemble sensitivity is 0.917 with a false positive rate of 0.038 in the results section and 4.1% in the conclusion.
- Section V is headed "Expected Results and Discussion" and states empirical validation is ongoing, so the abstract's headline numbers are not clearly measured outcomes.
- Section IV.D introduces an unexplained second framework name, "SENA-GR", and the reference list contains eleven unrelated power-electronics entries labelled Fig. 1 to Fig. 11.

## Cited Works

- Sharma, P.; Patel, V. (2022) (context) — Survey of information overload among digital payment users. [p. 1159]
- Hochreiter, S.; Schmidhuber, J. (1997) (methodology) — Long short-term memory; the recurrent baseline underpinning sequence modeling for financial text. [p. 1159]
- Mikolov, T.; Chen, K.; Corrado, G.; Dean, J. (2013) (methodology) — Word2Vec word embeddings; the origin point of the paper's account of NLP progress. [p. 1159]
- Graves, A.; Mohamed, A.; Hinton, G. (2013) (methodology) — Deep recurrent neural networks for speech recognition. [p. 1159]
- Vaswani, A.; Shazeer, N.; Parmar, N. et al. (2017) (methodology) — The transformer architecture, the basis of the encoder used here. [p. 1159]
- Devlin, J.; Chang, M.; Lee, K.; Toutanova, K. (2019) (methodology) — BERT, the pre-training scheme the framework inherits through MuRIL and FinBERT. [p. 1159]
- Kumar, R.; Singh, S.; Gupta, A. (2022) (context) — Digital payment adoption in India. [p. 1159]
- Chen, M.; Zhang, Y.; Wang, L. (2021) (context) — Longitudinal study of why people abandon expense tracking. [p. 1159]
- Smith, J.; Johnson, K. (2018) (baseline) — Rule-based financial entity extraction from SMS messages. [p. 1160]
- Kumar, V.; Sharma, S.; Gupta, P. (2019) (baseline) — Rule-based transaction extraction from bank SMS alerts, reaching 89% accuracy across five Indian banks. [p. 1160]
- Brown, T.; Wilson, S.; Davis, R. (2018) (baseline) — Machine learning for personal expense categorization. [p. 1160]
- Lee, S.; Kim, J. (2022) (baseline) — Few-shot learning for personalized expense categorization; 94.7% user satisfaction against 78.3% for non-personalized baselines. [p. 1160]
- Liu et al. (year not reported) (baseline) — BiLSTM-CRF financial named entity recognition; cited in text as [24] but absent from the reference list. [Not reported]
- Sharma and Gupta (year not reported) (baseline) — BiLSTM-CRF transaction extraction, 92.3% F1 on 8,000 messages; cited in text as [22] but absent from the reference list. [Not reported]
- Wang et al. (year not reported) (baseline) — Hierarchical attention network for transaction classification, 91.2% accuracy; cited in text as [21] but absent from the reference list. [Not reported]
- Ahmed et al. (year not reported) (baseline) — LSTM autoencoder fraud detection, 89.2% sensitivity at 4.7% false positive rate; cited in text as [18] but absent from the reference list. [Not reported]
- Wang et al. (year not reported) (baseline) — Graph neural network fraud detection with a 15% precision improvement; cited in text as [19] but absent from the reference list. [Not reported]
- Araci, D. (year not reported) (baseline) — FinBERT, the English-only financial BERT fine-tuned here as a comparison model; cited in text as [19] but absent from the reference list. [Not reported]
- Khanuja et al. (year not reported) (methodology) — MuRIL, the multilingual Indian-language BERT that initializes the proposed encoder; cited in text as [20] but absent from the reference list. [Not reported]
- Ahmed, A.; Mahmood, N. (year not reported) (baseline) — Hybrid rule-plus-statistical-plus-deep fraud system, 91.7% sensitivity at 3.8% false positive rate; cited in text as [32] but absent from the reference list. [Not reported]
- Nagarajan, C.; Madheswaran, M. (2011, 2012) and others (context) — Power-electronics articles on series parallel resonant converters, CLL-T converters and BLDC machines, printed in the reference block as "Fig. 1" to "Fig. 11" and unrelated to this paper's subject. [pp. 1159-1160]
- Tamilselvi, S.; Prakash, R.; Nagarajan, C. (2025, 2026) (context) — Smart grid ANN control and multilevel inverter sliding mode control, also printed under the figure block and unrelated to this paper. [p. 1159]
- Mullainathan, S.; Natarajan, R. (2025) and Suganthi, M.; Ramesh, N. (2022) (context) — Ceramic-materials quality assessment and zeolite membrane water filtration, also printed under the figure block and unrelated to this paper. [p. 1160]