---
paper_id: A--Huang-2025
first_author: "Huang"
year: 2025
title: "Dynamic Calibration of Decision Thresholds for Financial Anomaly Detection: Verification With Payment Platform Information and Data"
venue: "Journal of Global Information Management, 33(1), 1-26"
doi: 10.4018/JGIM.395852
type: journal-article
designation: algorithm
status: extracted
modules: [model_algorithm_integration, model_performance_evaluation, system_performance_evaluation]
module_rationale:
  model_algorithm_integration: "Sect. 3.1 (p. 5) wires four components into one streaming detector — sliding-window segmentation (Sec. 3.2), a temporal-attention encoder (Sec. 3.3), Isolation Forest scoring (Sec. 3.4) and a dynamic threshold calibration loop (Sec. 3.5) — and Sec. 3.6 (p. 9) runs the loop prequentially so scores, attention cues and the decision boundary advance together."
  model_performance_evaluation: "Sec. 5 (pp. 14-19) reports eight experiments over five payment datasets and six baselines — Table 2 (p. 15) precision/recall/F1/AUC/latency on IEEE-CIS, component ablations in Tables 3-4 (p. 16), concept-drift response in Table 5 (p. 17), window analysis in Table 6 (p. 18), minority-class detection in Table 7 (p. 19) and cross-dataset transfer in Table 8 (p. 19)."
  system_performance_evaluation: "Sec. 4.2 (p. 11) evaluates the operating point against a fixed alert budget and reviewer capacity and reports tail latency, and Sec. 6 (p. 21) reports that stabilised alert volumes cut manual review time by around 12% in pilot replay, with overhead under 8% CPU and about 25-30k transactions per second."
---

# Dynamic Calibration of Decision Thresholds for Financial Anomaly Detection: Verification With Payment Platform Information and Data

`A--Huang-2025` — Huang (2025), *Journal of Global Information Management, 33(1), 1-26* \[10.4018/JGIM.395852]

## Summary

Treating the alert threshold as an adaptive component rather than a fixed cutoff, TA-IFDC combines Isolation Forest scoring with a temporal-attention encoder and an online percentile-based calibration loop, holding F1 at 0.902-0.927 across five payment datasets while cutting drift-induced F1 loss to -0.012.

## Problem and Motivation

Global losses attributed to payment fraud are placed at more than USD 45 billion in 2022, and fraud patterns are described as increasingly fragmented and adaptive, which makes early detection of suspicious transactions more complex (Sec. 1 Introduction, p. 2). Isolation Forest is widely used for unsupervised screening because it is fast on large datasets and needs no labels, but production deployments typically fix the anomaly-score cutoff during an initial calibration or choose it heuristically and then leave it in place (Sec. 1, p. 2). Real payment traffic does not stand still: seasonal campaigns, macro shifts and coordinated rings all move the score distribution, so a static line either floods reviewers during benign surges or misses gradual shifts, while labels for feedback usually arrive late or not at all (Sec. 1, p. 2).

## Method

**Design.** Empirical algorithm-development study: a proposed framework (TA-IFDC) benchmarked on five payment datasets against six baselines over eight experiments, including two component ablations, an induced-concept-drift test, a sliding-window-size analysis, minority-class detection and cross-dataset transfer; the authors state no formal design label.
**Sample.** Five public or simulated payment transaction datasets used separately — IEEE-CIS Fraud Detection (more than one million labelled online transactions, around 3.5% fraud), PaySim (over 6 million synthetic mobile-money transactions, approximately 0.13% fraud), CCFD (approximately 285,000 European credit-card transactions, 0.172% fraud), SFD-FD (IBM synthetic corpus with controllable drift events) and BankSim (multi-agent simulated retail-bank transactions); unit: one transaction, grouped into overlapping sliding windows and split 80%/10%/10% by time. A pooled total is Not reported, because the datasets are never combined.
**Context.** geography: Not reported (the datasets are international; PaySim simulates sub-Saharan African mobile money and CCFD comes from a European card issuer); population: Not reported — no human participants, the records being anonymised or synthetic transactions; setting: offline/virtual evaluation of a streaming detector on a workstation with an Intel i9 CPU, 64 GB RAM and one NVIDIA RTX 3090 GPU.

- Segment the incoming transaction stream into overlapping sliding windows of size W with stride S, so a window is the processing unit for detection and for online threshold adaptation (Sec. 3.2, p. 6).
- Encode each timestamp as a time-encoding vector e = φ(t) in R^h, using a Fourier-based positional encoding or a learned embedding, and concatenate it with the transaction's feature vector (Sec. 3.3, p. 6).
- Apply scaled dot-product attention across the window so each transaction is reweighted by its temporal relevance, yielding attention-enhanced context vectors z_i (Sec. 3.3, p. 6).
- Score every attention-enhanced vector with an Isolation Forest ensemble, where s(z_i) = 2^(−E(h(z_i))/c(n)) and a score close to 1 indicates high anomaly probability (Sec. 3.4, p. 7).
- Recalibrate the decision threshold in every window by blending the previous threshold with the β-th percentile of current scores, θ_k = (1−λ)·θ_(k−1) + λ·Quantile_β(S_k), initialised from the first window (Sec. 3.5.1, p. 7).
- Optionally correct that threshold from delayed ground truth, adding Δθ_k = η·(α·FP_k/W − (1−α)·FN_k/W) to θ_k once confirmed fraud labels are available (Sec. 3.5.2, pp. 7-8).
- Choose the operating quantile by ablation across the 90-99 percentiles, settling on 95% because false positives surge below about 93% and recall falls sharply above about 97%; hysteresis and adaptive smoothing cap per-window change at approximately 2-3% of the prior value (Sec. 3.6, p. 9).
- Monitor drift with a lightweight detector on the Kolmogorov-Smirnov distance between incoming and historical feature distributions; when drift is significant at p<0.01 the calibrator's state is partially reset for the new regime (Sec. 4.4, p. 14).
- Run the detector prequentially in mini-batch and online mode: score each arriving transaction against the current boundary, route records above the cutoff to risk controls, then slide the window pointer and recalibrate on the next slice (Sec. 3.6, p. 9).
- Evaluate on the five datasets against Online-iForest, Hybrid AI-Fraud, GNN-IF, SSR-RVFL and XGB-Anomaly plus an autoencoder detector, reporting precision, recall, F1, AUC and P95/P99 latency under time-split, injected-drift and delayed-label protocols (Sec. 4.2-4.3, pp. 11-12; Sec. 5, pp. 14-19).

## Software

- Python 3.10
- scikit-learn (version not reported; archived in the supplementary material)
- PyTorch (version not reported)
- PyOD (version not reported)
- DGL (version not reported)
- Baseline detectors reimplemented in Python: Online-iForest (tree depth 10, 64 histogram bins), GNN-based models (two graph convolution layers, ReLU, 32-dimensional embeddings), AE-Fraud (bottleneck 16, Adam, learning rate 1e-3, 30 epochs, mean squared reconstruction loss), LOF (k=20) and XGBoost-Fraud (maximum tree depth 6, early stopping on AUC) (Sec. 4.4, p. 14)
- Hardware: Intel i9 CPU, 64 GB RAM, one NVIDIA RTX 3090 GPU (Sec. 4.4, p. 14)

## Key Findings

- num: Table 2 (p. 15) gives TA-IFDC precision 0.936, recall 0.918, F1 0.927 and AUC 0.974 on IEEE-CIS, against F1 of 0.853 for Online-iForest, 0.884 for Hybrid AI-Fraud, 0.877 for GNN-IF, 0.910 for SSR-RVFL and 0.836 for XGB-Anomaly.
- num: Per-record latency on IEEE-CIS is 29 ms for TA-IFDC against 22 ms (Online-iForest), 68 ms (Hybrid AI-Fraud), 54 ms (GNN-IF), 49 ms (SSR-RVFL) and 34 ms (XGB-Anomaly) (Table 2, p. 15).
- num: Ablating the dynamic threshold calibration on IEEE-CIS moves precision from 0.936 to 0.871, recall from 0.918 to 0.835, F1 from 0.927 to 0.852 and AUC from 0.974 to 0.923, at 31 ms instead of 29 ms (Table 3, p. 16).
- num: Ablating the temporal attention on PaySim moves precision from 0.918 to 0.877, recall from 0.904 to 0.848, F1 from 0.911 to 0.862 and AUC from 0.968 to 0.938, at 29 ms instead of 28 ms (Table 4, p. 16).
- num: Under induced concept drift on SFD-FD, F1 falls from 0.914 to 0.902 for TA-IFDC (ΔF1 of -0.012), against 0.869 to 0.784 for Online-iForest (-0.085) and 0.888 to 0.821 for SSR-RVFL (-0.067) (Table 5, p. 17).
- num: On BankSim, TA-IFDC holds F1 of 0.909, 0.912 and 0.905 across the 24h, 48h and 72h windows at 26, 29 and 31 ms latency, against Online-iForest at 0.846, 0.842 and 0.834 with 21, 23 and 25 ms (Table 6, p. 18).
- num: On the 0.172%-fraud CCFD minority class, TA-IFDC reaches precision 0.903, recall 0.889 and F1 0.896, against SSR-RVFL at 0.864, 0.850 and 0.857 and XGB-Anomaly at 0.788, 0.741 and 0.764 (Table 7, p. 19).
- num: Trained on PaySim and tested on CCFD without fine-tuning, TA-IFDC records F1 0.841 and AUC 0.904, against SSR-RVFL at 0.798 and 0.878 and Online-iForest at 0.772 and 0.856 (Table 8, p. 19).
- num: Operational overhead is reported as less than 8% CPU above a static Isolation Forest pipeline at approximately 25-30k transactions per second on standard CPUs, energy below 0.5 Wh per 1k transactions, and a reduction in manual review time of around 12% in pilot replay (Sec. 6 Discussion, p. 21).
- num: Sec. 7 (p. 22) states that across the five datasets latency stayed flat at around 35 ms per record (P95), while Tables 2-6 print 26-31 ms.

## Key Figures and Tables

- Fig. 1 (p. 5): Overview of the main processing stages in TA-IFDC → the four components (sliding window, temporal attention encoder, Isolation Forest scoring, dynamic threshold calibration) execute in that order on each window.
- Table 1 (pp. 13-14): Comparison of the baseline models by supervision, temporal adaptation, threshold mechanism and strengths → every comparator except SSR-RVFL is listed with a fixed or heuristic threshold, which is the gap TA-IFDC targets.
- Fig. 2 (p. 15): IEEE-CIS overall results, panel (a) sorted by F1 and panel (b) ranked by latency → TA-IFDC leads on F1 and AUC while Online-iForest is the fastest model.
- Table 2 (p. 15): Overall performance comparison on IEEE-CIS → F1 0.927 and AUC 0.974 at 29 ms is the best reported pair among the six models.
- Fig. 3 (p. 16): Effect of dynamic threshold calibration on IEEE-CIS → the ablation isolates what the calibration loop alone contributes.
- Table 3 (p. 16): Effect of dynamic threshold calibration → recall 0.918 to 0.835 and F1 0.927 to 0.852 once the module is removed.
- Table 4 (p. 16): Impact of the temporal attention mechanism → F1 0.911 against 0.862 and AUC 0.968 against 0.938 without attention.
- Fig. 4 (p. 17): ROC curves for TA-IFDC with and without temporal attention on PaySim, with the random-classifier reference at 0.5 AUC → the attention variant ranks fraud above legitimate transactions better.
- Table 5 (p. 17): Concept drift response on SFD-FD → TA-IFDC loses 0.012 F1 where the static baselines lose 0.085 and 0.067.
- Fig. 5 (p. 18): Performance comparison before and after concept drift on SFD-FD → the gap between the adaptive model and the static baselines widens after the injected drift.
- Table 6 (p. 18): Online window analysis on BankSim → TA-IFDC F1 stays near 0.91 for 24h-72h windows while latency rises from 26 ms to 31 ms.
- Fig. 6 (p. 19): F1-score and latency across window sizes on BankSim → Online-iForest is marginally faster but its F1 falls below 0.84 at longer windows.
- Table 7 (p. 19): Minority class detection on CCFD → F1 0.896 for TA-IFDC on the dataset where most models falter because of the 0.172% fraud rate.
- Fig. 7 (p. 20): Minority class detection and cross-dataset generalization side by side on CCFD → the same two CCFD evaluations appear as panels.
- Table 8 (p. 19): Cross-dataset generalization, train PaySim then test CCFD → F1 0.841 and AUC 0.904 without fine-tuning.

## Limitations and Gaps

- The authors' own most significant limitation is the dependence on continuous, time-stamped transaction streams: efficacy may still depend on the availability of timestamps and partial temporal continuity, so legacy banking stacks with coarse or inconsistent logging may need ordering and clock-alignment shims and may reduce the reliability of anomaly scoring (Sec. 6 Discussion, p. 21; Sec. 7 Conclusion, p. 22).
- The authors acknowledge that the feedback module recalibrates through "a soft adjustment of decision thresholds derived from patterns of historical model consensus", so direct supervisory signals such as confirmed-fraud annotations from domain experts or real-time user reports are not yet part of the recalibration process (Sec. 6 Discussion, p. 21).
- The authors acknowledge that the label-free fallback mode is imperfect: when feedback dries up the system relies only on the scoring trend, and "over time, recall tends to slide a bit", while alert volume stays stable and false alarms low (Sec. 6 Discussion, p. 21).
- The authors acknowledge that external feedback such as analyst decisions, customer reports and inter-bank intelligence should help under extreme imbalance, but that privacy and integration constraints must be handled (Sec. 7 Conclusion, p. 22).
- Transformer-based detectors were excluded from the benchmark because of dense supervision needs and higher GPU inference cost, so the temporal-attention claim is never compared against a transformer detector, which the paper calls a strong candidate for future comparative study (the Baseline Methods subsection, p. 13).
- [unacknowledged] The comparator set is named inconsistently: the Baseline Methods subsection (p. 11) lists Online-iForest, Hybrid-AI, GNN-IF, XGB-Anomaly, SSR-RVFL and an autoencoder detector, then describes Hybrid-GNN-AE, ONLINE-IFOREST, Adaptive IF + LSTM, Enhanced IForest, Hybrid-AI-FD and SSR-RVFL, Table 1 (pp. 13-14) lists a different set including a "Graph Temporal Embedding" row, and Table 2 (p. 15) compares only TA-IFDC, Online-iForest, Hybrid AI-Fraud, GNN-IF, SSR-RVFL and XGB-Anomaly.
- [unacknowledged] Reported latency is internally inconsistent: Tables 2-6 (pp. 15-18) print 26-31 ms per record, while Sec. 7 (p. 22) states latency "stayed flat at around 35 ms per record (P95)". Neither figure can be reconciled from the paper.
- [unacknowledged] The Hyperparameter Settings and Training Strategy subsection (p. 14) claims results are reported as mean ± standard deviation with 95% bootstrap confidence intervals over five independent seeds, but no standard deviation, confidence interval, per-seed value or p-value appears in any of Tables 2-8.
- [unacknowledged] The Evaluation Metrics subsection (p. 11) reports tail latency "within about 1.4 times the average" under peak load, yet no P95 or P99 figure is tabulated, and the drift guardrails are given inconsistently as "±1–2%" and as a cap of "≈2–3%" of the prior value (the Overall Algorithm Description subsection, p. 9).
- [unacknowledged] The decision boundary is a smoothed high percentile of Isolation Forest anomaly scores, not a quartile statistic: the paper reports no inter-quartile range, no quartile fences and no quartile-based baseline, so its threshold cannot be compared with quartile outlier rules (the Adaptive Threshold Update Rule subsection, p. 7; the Overall Algorithm Description subsection, p. 9).
- [unacknowledged] The symbol α carries three unrelated meanings — the precision/recall balance in the feedback correction, the momentum smoothing factor fixed at 0.1, and the attention softmax normalisation — while λ is the adaptivity coefficient of the percentile update (the threshold-calibration subsections, pp. 7-8; the Hyperparameter Settings and Training Strategy subsection, p. 14).
- [unacknowledged] The original Isolation Forest is attributed to "Liu et al." but no Liu entry appears anywhere in the reference list, so the founding citation is unresolvable from the paper (Sec. 2 Related Work, p. 3; Refs. pp. 24-25).
- [unacknowledged] Eight experiments run on five datasets, but each ablation appears on one dataset only, and no precision-recall curve, alert-volume time series, false-positive count or reviewer-level outcome is tabulated anywhere, so the alert-budget claim rests on aggregate precision alone (Sec. 5, pp. 14-19; Sec. 6, p. 21).
- [unacknowledged] No human study, live deployment or labelled production stream is involved: every number comes from four public or simulated benchmarks plus one synthetic drift corpus, and the 12% manual-review reduction is described only as "pilot replay" (Sec. 6 Discussion, p. 21).

## Definitions

- **Isolation Forest (IF)** — an unsupervised detector that builds random partition trees by choosing attributes and split values at random, so points departing from the bulk are isolated in only a few splits and have short path lengths (Sec. 1 Introduction, p. 2).
- **TA-IFDC** — Temporal-Attention Isolation Forest with Dynamic Calibration, the framework the paper proposes (Abstract, p. 1).
- **Dynamic Threshold Calibration (DTC)** — the module that adaptively adjusts θ for each sliding window using recent prediction feedback statistics (Sec. 3.5, p. 7).
- **Quantile_β** — the function returning the β-th percentile of a window's anomaly scores, for example β=0.95 for the top 5% anomaly (Sec. 3.5.1, p. 7).
- **Adaptive coefficient (λ)** — the learning rate in [0,1] that sets how fast the threshold follows the score distribution (Sec. 3.5.1, p. 7).
- **Feedback gain (η)** — the tuning parameter scaling the delayed-label correction applied to the threshold (Sec. 3.5.2, p. 8).
- **Anomaly score** — the Isolation Forest score s(z_i); a score close to 1 indicates high anomaly probability (Sec. 3.4, p. 7).
- **Sliding window** — the segment of W consecutive transactions taken with stride S that serves as the processing unit for detection and threshold adaptation (Sec. 3.2, p. 6).
- **Prequential (online) loop** — the deployment mode in which the threshold moves with the stream instead of being frozen at launch, so the model is no longer a train-once-and-ship artifact (Sec. 3.6, p. 9; Sec. 7, p. 22).
- **Concept drift** — artificial behavioural changes introduced at defined intervals to simulate evolving fraud patterns (Sec. 5 Experiment 4, p. 17).
- **Alert budget** — the reviewer-capacity constraint under which the operating point is chosen, so precision-recall behaviour stays tied to reviewer capacity and loss-prevention costs (Sec. 4.2, p. 11).
- **Kolmogorov-Smirnov distance** — the statistic a lightweight drift detector monitors between incoming and historical feature distributions (Sec. 4.4, p. 14).

## Key Equations

- `T = {x_1, x_2, ..., x_N}, x_i ∈ R^d` — the incoming transaction stream, one transaction with d features.
- `W_k = {x_{kS}, ..., x_{kS+W-1}}, k = 1, ..., K` — the k-th overlapping window of size W taken with stride S.
- `x_tilde_{k,j} = concat(x_{k,j}, e_{k,j})` — transaction vector concatenated with its time-encoding vector.
- `alpha_ij = softmax_j(q_i^T k_j / sqrt(d_k))` — scaled dot-product attention weight of transaction i over the window.
- `z_i = sum_j alpha_ij · (W_V x_tilde_{k,j})` — attention-enhanced context vector passed to Isolation Forest scoring.
- `s(z_i) = 2^(-E(h(z_i))/c(n))` — anomaly score from average path length; close to 1 means high anomaly probability.
- `c(n) = 2H(n-1) - 2(n-1)/n` — normalisation factor converting average path length to a score.
- `H(i) = ln(i) + gamma, gamma ≈ 0.5772` — the harmonic number used inside c(n).
- `theta_k = (1 - lambda)·theta_{k-1} + lambda·Quantile_beta(S_k)` — smoothed percentile update of the decision threshold per window.
- `delta_theta_k = eta·(alpha·FP_k/W - (1-alpha)·FN_k/W)` — delayed-label correction; theta_k is then set to theta_k + delta_theta_k.
- `F1 = 2·Precision·Recall / (Precision + Recall)` — harmonic summary of the false-alarm and miss trade-off.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| IEEE-CIS fraud detection, TA-IFDC (proposed) | precision | 0.936 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, TA-IFDC (proposed) | recall | 0.918 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, TA-IFDC (proposed) | F1 | 0.927 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, TA-IFDC (proposed) | AUC | 0.974 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, TA-IFDC (proposed) | latency (ms) | 29 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, Online-iForest baseline | precision | 0.862 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, Online-iForest baseline | recall | 0.845 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, Online-iForest baseline | F1 | 0.853 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, Online-iForest baseline | AUC | 0.931 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, Online-iForest baseline | latency (ms) | 22 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, Hybrid AI-Fraud baseline | precision | 0.892 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, Hybrid AI-Fraud baseline | recall | 0.877 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, Hybrid AI-Fraud baseline | F1 | 0.884 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, Hybrid AI-Fraud baseline | AUC | 0.944 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, Hybrid AI-Fraud baseline | latency (ms) | 68 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, GNN-IF baseline | precision | 0.884 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, GNN-IF baseline | recall | 0.871 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, GNN-IF baseline | F1 | 0.877 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, GNN-IF baseline | AUC | 0.942 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, GNN-IF baseline | latency (ms) | 54 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, SSR-RVFL baseline | precision | 0.915 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, SSR-RVFL baseline | recall | 0.906 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, SSR-RVFL baseline | F1 | 0.910 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, SSR-RVFL baseline | AUC | 0.961 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, SSR-RVFL baseline | latency (ms) | 49 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, XGB-Anomaly baseline | precision | 0.851 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, XGB-Anomaly baseline | recall | 0.823 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, XGB-Anomaly baseline | F1 | 0.836 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, XGB-Anomaly baseline | AUC | 0.918 | — | — | Table 2, p. 15 |
| IEEE-CIS fraud detection, XGB-Anomaly baseline | latency (ms) | 34 | — | — | Table 2, p. 15 |
| Dynamic-threshold ablation, full TA-IFDC | precision | 0.936 | — | — | Table 3, p. 16 |
| Dynamic-threshold ablation, full TA-IFDC | recall | 0.918 | — | — | Table 3, p. 16 |
| Dynamic-threshold ablation, full TA-IFDC | F1 | 0.927 | — | — | Table 3, p. 16 |
| Dynamic-threshold ablation, full TA-IFDC | AUC | 0.974 | — | — | Table 3, p. 16 |
| Dynamic-threshold ablation, full TA-IFDC | latency (ms) | 29 | — | — | Table 3, p. 16 |
| Dynamic-threshold ablation, TA-IFDC without DynThreshold | precision | 0.871 | — | — | Table 3, p. 16 |
| Dynamic-threshold ablation, TA-IFDC without DynThreshold | recall | 0.835 | — | — | Table 3, p. 16 |
| Dynamic-threshold ablation, TA-IFDC without DynThreshold | F1 | 0.852 | — | — | Table 3, p. 16 |
| Dynamic-threshold ablation, TA-IFDC without DynThreshold | AUC | 0.923 | — | — | Table 3, p. 16 |
| Dynamic-threshold ablation, TA-IFDC without DynThreshold | latency (ms) | 31 | — | — | Table 3, p. 16 |
| Temporal-attention ablation, full TA-IFDC on PaySim | precision | 0.918 | — | — | Table 4, p. 16 |
| Temporal-attention ablation, full TA-IFDC on PaySim | recall | 0.904 | — | — | Table 4, p. 16 |
| Temporal-attention ablation, full TA-IFDC on PaySim | F1 | 0.911 | — | — | Table 4, p. 16 |
| Temporal-attention ablation, full TA-IFDC on PaySim | AUC | 0.968 | — | — | Table 4, p. 16 |
| Temporal-attention ablation, full TA-IFDC on PaySim | latency (ms) | 28 | — | — | Table 4, p. 16 |
| Temporal-attention ablation, TA-IFDC without Attention | precision | 0.877 | — | — | Table 4, p. 16 |
| Temporal-attention ablation, TA-IFDC without Attention | recall | 0.848 | — | — | Table 4, p. 16 |
| Temporal-attention ablation, TA-IFDC without Attention | F1 | 0.862 | — | — | Table 4, p. 16 |
| Temporal-attention ablation, TA-IFDC without Attention | AUC | 0.938 | — | — | Table 4, p. 16 |
| Temporal-attention ablation, TA-IFDC without Attention | latency (ms) | 29 | — | — | Table 4, p. 16 |
| Concept-drift response on SFD-FD, TA-IFDC | F1 (Pre-drift) | 0.914 | — | — | Table 5, p. 17 |
| Concept-drift response on SFD-FD, TA-IFDC | F1 (Post-drift) | 0.902 | — | — | Table 5, p. 17 |
| Concept-drift response on SFD-FD, TA-IFDC | ΔF1 | -0.012 | — | — | Table 5, p. 17 |
| Concept-drift response on SFD-FD, Online-iForest | F1 (Pre-drift) | 0.869 | — | — | Table 5, p. 17 |
| Concept-drift response on SFD-FD, Online-iForest | F1 (Post-drift) | 0.784 | — | — | Table 5, p. 17 |
| Concept-drift response on SFD-FD, Online-iForest | ΔF1 | -0.085 | — | — | Table 5, p. 17 |
| Concept-drift response on SFD-FD, SSR-RVFL | F1 (Pre-drift) | 0.888 | — | — | Table 5, p. 17 |
| Concept-drift response on SFD-FD, SSR-RVFL | F1 (Post-drift) | 0.821 | — | — | Table 5, p. 17 |
| Concept-drift response on SFD-FD, SSR-RVFL | ΔF1 | -0.067 | — | — | Table 5, p. 17 |
| BankSim online window analysis, TA-IFDC 24h window | F1 | 0.909 | — | — | Table 6, p. 18 |
| BankSim online window analysis, TA-IFDC 24h window | latency (ms) | 26 | — | — | Table 6, p. 18 |
| BankSim online window analysis, TA-IFDC 48h window | F1 | 0.912 | — | — | Table 6, p. 18 |
| BankSim online window analysis, TA-IFDC 48h window | latency (ms) | 29 | — | — | Table 6, p. 18 |
| BankSim online window analysis, TA-IFDC 72h window | F1 | 0.905 | — | — | Table 6, p. 18 |
| BankSim online window analysis, TA-IFDC 72h window | latency (ms) | 31 | — | — | Table 6, p. 18 |
| BankSim online window analysis, Online-iForest 24h window | F1 | 0.846 | — | — | Table 6, p. 18 |
| BankSim online window analysis, Online-iForest 24h window | latency (ms) | 21 | — | — | Table 6, p. 18 |
| BankSim online window analysis, Online-iForest 48h window | F1 | 0.842 | — | — | Table 6, p. 18 |
| BankSim online window analysis, Online-iForest 48h window | latency (ms) | 23 | — | — | Table 6, p. 18 |
| BankSim online window analysis, Online-iForest 72h window | F1 | 0.834 | — | — | Table 6, p. 18 |
| BankSim online window analysis, Online-iForest 72h window | latency (ms) | 25 | — | — | Table 6, p. 18 |
| CCFD minority-class detection, TA-IFDC | precision | 0.903 | — | — | Table 7, p. 19 |
| CCFD minority-class detection, TA-IFDC | recall | 0.889 | — | — | Table 7, p. 19 |
| CCFD minority-class detection, TA-IFDC | F1 | 0.896 | — | — | Table 7, p. 19 |
| CCFD minority-class detection, SSR-RVFL | precision | 0.864 | — | — | Table 7, p. 19 |
| CCFD minority-class detection, SSR-RVFL | recall | 0.850 | — | — | Table 7, p. 19 |
| CCFD minority-class detection, SSR-RVFL | F1 | 0.857 | — | — | Table 7, p. 19 |
| CCFD minority-class detection, XGB-Anomaly | precision | 0.788 | — | — | Table 7, p. 19 |
| CCFD minority-class detection, XGB-Anomaly | recall | 0.741 | — | — | Table 7, p. 19 |
| CCFD minority-class detection, XGB-Anomaly | F1 | 0.764 | — | — | Table 7, p. 19 |
| Cross-dataset generalization PaySim to CCFD, TA-IFDC | F1 | 0.841 | — | — | Table 8, p. 19 |
| Cross-dataset generalization PaySim to CCFD, TA-IFDC | AUC | 0.904 | — | — | Table 8, p. 19 |
| Cross-dataset generalization PaySim to CCFD, SSR-RVFL | F1 | 0.798 | — | — | Table 8, p. 19 |
| Cross-dataset generalization PaySim to CCFD, SSR-RVFL | AUC | 0.878 | — | — | Table 8, p. 19 |
| Cross-dataset generalization PaySim to CCFD, Online-iForest | F1 | 0.772 | — | — | Table 8, p. 19 |
| Cross-dataset generalization PaySim to CCFD, Online-iForest | AUC | 0.856 | — | — | Table 8, p. 19 |
| Operating quantile chosen after ablation across the 90-99 percentiles | quantile | 95% | — | — | Sec. 3.6 Overall Algorithm Description, p. 9 |
| Quantile below which false positives surge | percentile | ~93% | — | — | Sec. 3.6 Overall Algorithm Description, p. 9 |
| Quantile above which recall falls sharply | percentile | ~97% | — | — | Sec. 3.6 Overall Algorithm Description, p. 9 |
| Per-window threshold change cap under hysteresis and smoothing | percentage of prior value | ≈2-3% | — | — | Sec. 3.6 Overall Algorithm Description, p. 9 |
| Drift-detector significance threshold on the Kolmogorov-Smirnov distance | p | <0.01 | — | <0.01 | Sec. 4.4 Hyperparameter Settings, p. 14 |
| Tail latency relative to the average under peak load | ratio | about 1.4 times the average | — | — | Sec. 4.2 Evaluation Metrics, p. 11 |
| Base Isolation Forest configuration | trees / subsample size | 100 trees; subsampling size of 256 | — | — | Sec. 4.4 Hyperparameter Settings, p. 14 |
| Sliding calibration window and update interval | transactions / steps | sliding calibration window of size 2,000 transactions, updated every 100 steps | — | — | Sec. 4.4 Hyperparameter Settings, p. 14 |
| Temporal attention block configuration | heads / past window | two-head attention block attending to a past window of 15 steps | — | — | Sec. 4.4 Hyperparameter Settings, p. 14 |
| Momentum smoothing factor of the threshold update | smoothing factor | α=0.1 | — | — | Sec. 4.4 Hyperparameter Settings, p. 14 |
| Operational CPU overhead above a static Isolation Forest pipeline | overhead | less than 8% CPU | — | — | Sec. 6 Discussion, p. 21 |
| Sustained throughput on standard CPUs | transactions per second | approximately 25-30k transactions per second | — | — | Sec. 6 Discussion, p. 21 |
| Energy consumption per 1 k transactions | energy | below 0.5 Wh per 1 k transactions | — | — | Sec. 6 Discussion, p. 21 |
| Reduction in manual review time after stabilising alert volumes | reduction | around 12% | — | — | Sec. 6 Discussion, p. 21 |
| Per-record latency stated in the conclusion | latency (P95) | around 35 ms per record | — | — | Sec. 7 Conclusion, p. 22 |
| IEEE-CIS dataset fraud rate | prevalence | around 3.5% | — | — | Sec. 4.1 Datasets, p. 10 |
| IEEE-CIS dataset fraud rate, stated as a proportion | prevalence | roughly one in twenty-eight | — | — | Sec. 4.1 Datasets, p. 10 |
| PaySim dataset fraud prevalence | prevalence | approximately 0.13% | — | — | Sec. 4.1 Datasets, p. 10 |
| CCFD dataset fraud rate | prevalence | 0.172% | — | — | Sec. 4.1 Datasets, p. 10 |
| Global payment fraud losses cited in the introduction | losses | more than USD 45 billion in 2022 | — | — | Sec. 1 Introduction, p. 2 |
| Train/validation/test partition by time | split | 80%/10%/10% | — | — | Sec. 4 Experimental Setup, p. 9 |
| Comparative experiments reported | experiments | eight rounds of comparative tests | — | — | Sec. 5 Experimental Results, p. 14 |
| Benchmark datasets used | datasets | five — IEEE-CIS, PaySim, CCFD, SFD-FD, BankSim | — | — | Sec. 4.1 Datasets, p. 10 |
| Baselines benchmarked | baselines | six | — | — | Sec. 1 Introduction, p. 2 |
| Repeated runs behind the reported metrics | runs | five independent runs with different random seeds | — | — | Sec. 4.4 Hyperparameter Settings, p. 14 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The method monitors the evolving distribution of IF scores in streaming mode and updates the decision boundary online, while a lightweight temporal-attention module encodes short-range dependencies across consecutive transactions." | Abstract, p. 1 | model_algorithm_integration |
| "A dynamic calibration step updates the decision boundary online using recent score statistics and delayed outcomes, keeping alert rates stable while tracking distribution change" | Sec. 1 Introduction, p. 2 | model_algorithm_integration |
| "Experience with IF in production exposes a weak spot: decisions usually depend on a fixed score cutoff set during an initial calibration or chosen heuristically, then left in place." | Sec. 1 Introduction, p. 2 | system_performance_evaluation |
| "A static line can flood reviewers during benign surges or miss gradual shifts that matter; both outcomes degrade performance." | Sec. 1 Introduction, p. 2 | system_performance_evaluation |
| "In financial settings the asymmetry is costly—missed fraud yields direct loss, while excessive alerts erode reviewer trust and inflate operational budgets." | Sec. 2 Related Work, p. 4 | system_performance_evaluation |
| "Calibrating decision thresholds remains underexplored relative to model design in anomaly detection." | Sec. 2 Related Work, p. 3 | model_algorithm_integration |
| "A dynamic threshold calibration mechanism is proposed, enabling IF to operate adaptively in non-stationary data environments without external supervision" | Sec. 1 Contributions, p. 3 | model_algorithm_integration |
| "This rule smooths threshold changes to prevent instability due to local score fluctuations." | Sec. 3.5.1 Adaptive Threshold Update Rule, p. 7 | model_algorithm_integration |
| "This formulation penalizes overly aggressive thresholds (high FP) and overly conservative thresholds (high FN), encouraging balance." | Sec. 3.5.2 Feedback-Informed Calibration, p. 8 | model_performance_evaluation |
| "Quantile selection was ablated across 90–99 percentiles. Below ~93% false positives surged; above ~97% recall fell sharply." | Sec. 3.6 Overall Algorithm Description, p. 9 | model_performance_evaluation |
| "Because payment streams are heavily imbalanced, accuracy is not informative." | Sec. 4.2 Evaluation Metrics, p. 11 | model_performance_evaluation |
| "Since a single number hides local behavior, we also examine the precision–recall neighborhood around the operating point chosen under a fixed alert budget so the analysis remains tied to reviewer capacity and loss-prevention costs." | Sec. 4.2 Evaluation Metrics, p. 11 | system_performance_evaluation |
| "In our tests, even under peak load, the longest delays stayed within about 1.4 times the average." | Sec. 4.2 Evaluation Metrics, p. 11 | system_performance_evaluation |
| "Removing the dynamic threshold module leads to significant performance degradation across all metrics, particularly recall." | Sec. 5 Experiment 2, p. 16 | model_performance_evaluation |
| "That said, this fallback mode isn't perfect: over time, recall tends to slide a bit." | Sec. 6 Discussion, p. 21 | model_performance_evaluation |
| "The much smaller drop for TA-IFDC (−0.012) suggests that its adaptive thresholding and feedback updates helped it maintain performance when the data distribution shifted." | Sec. 5 Experiment 4, p. 17 | model_performance_evaluation |
| "its efficacy may still depend on the availability of transaction timestamps and partial temporal continuity" | Sec. 6 Discussion, p. 21 | model_algorithm_integration |
| "By stabilizing alert volumes, TA-IFDC reduced manual review time by around 12% in pilot replay." | Sec. 6 Discussion, p. 21 | system_performance_evaluation |
| "Continuous, time-stamped streams are assumed; legacy stacks with coarse or asynchronous logging may need ordering and clock-alignment shims." | Sec. 7 Conclusion, p. 22 | model_algorithm_integration |
| "The current calibration loop leans on model-derived agreement signals; bringing in external feedback—analyst decisions, customer reports, inter-bank intelligence—should help under extreme imbalance, though privacy and integration constraints must be handled." | Sec. 7 Conclusion, p. 22 | model_algorithm_integration |

## Remember This

- TA-IFDC replaces the fixed anomaly-score cutoff with a smoothed 95th-percentile threshold recalculated every sliding window.
- Ablating the calibration loop costs the most recall: 0.918 to 0.835 and F1 0.927 to 0.852 on IEEE-CIS.
- Under injected drift on SFD-FD, TA-IFDC loses 0.012 F1 where Online-iForest loses 0.085.
- Cross-dataset transfer from PaySim to CCFD gives F1 0.841 and AUC 0.904 without fine-tuning.
- The boundary is a high percentile of Isolation Forest scores; no quartile or fence statistic appears.

## Cited Works

- Attar, A. A.; Bao, K.; Hagenmeyer, V.; Fabarisov, T.; Morozov, A. (2024) (context) — Cited for the framing of thresholding as a core part of the detector rather than post-processing, in a review and enhanced method for adaptive dynamic thresholds. [Sec. 1, p. 2]
- Al Lawati, H. M.; Zainal, A.; Al-Rimy, B. A. S.; et al. (2025) (context) — Cited with Lin et al. for updating the decision boundary online from recent score statistics and delayed outcomes in payment fraud detection. [Sec. 1, p. 2]
- Lin, C.; Du, B.; Sun, L.; Li, L. (2024) (context) — Cited for hierarchical context representation with self-adaptive thresholding in multivariate anomaly detection. [Sec. 1, p. 2]
- Zheng, Z.; Zhou, B.; Song, Y. (2025) (context) — Cited for the temporal-aware graph attention idea behind the lightweight short-range dependency component. [Sec. 1, p. 2]
- Sonani, R.; Govindarajan, V. (2022) (context) — Cited for the observation that seasonal campaigns, macro shifts and coordinated rings move the anomaly-score distribution in financial services compliance monitoring. [Sec. 1, p. 2]
- Vanini, P.; Rossi, S.; Zvizdic, E.; Domenig, T. (2023) (context) — Cited for online payment fraud streams in which labels arrive late or not at all. [Sec. 1, p. 2]
- Zhang, W.; Xu, Y.; Zheng, H.; Li, L. (2022) (context) — Cited for the estimate placing global payment fraud losses above USD 45 billion in 2022 and for increasingly fragmented fraud patterns. [Sec. 1, p. 2]
- Tokovarov, M.; Karczmarek, P. (2022) (context) — Cited for a probabilistic generalisation of Isolation Forest, attached to the contribution that temporal attention improves sequential or contextual anomaly detection. [Sec. 1 Contributions, p. 3]
- Hilal, W.; Gadsden, S. A.; Yawney, J. (2022) (methodology) — Cited with Al Farizi and Immadisetty for Isolation Forest isolating observations by randomly selecting features and split values. [Sec. 2, p. 3]
- Leveni, F.; Cassales, G. W.; Pfahringer, B.; Bifet, A.; Boracchi, G. (2025) (baseline) — Online Isolation Forest with incremental updates to the tree ensemble, cited for handling new transactions as they arrive. [Sec. 2, p. 3]
- Chen, T.; Tsourakakis, C. (2022) (context) — Antibenford subgraphs in financial networks, cited as the basis of the GNN-IF baseline's account-entity graph embedding. [Sec. 2, p. 3]
- Kim, H.; Lee, B. S.; Shin, W.-Y.; Lim, S. (2022) (context) — Cited with Chen and Tsourakakis for graph-based anomaly-detection formulations in financial data. [Sec. 2, p. 3]
- Almazroi, A. A.; Ayub, N. (2023) (context) — Online payment fraud detection with machine learning, cited among the supervised paradigms whose label dependence limits long-term maintainability. [Sec. 2, p. 4]
- Mazumder, M. T. R.; Shourov, M. S. H.; Rasul, I.; et al. (2025) (context) — Cited with Almazroi and Ayub for the range of detection paradigms from gradient-boosted trees to hybrid clustering and classification layers. [Sec. 2, p. 4]
- Eswar Prasad, G.; Hemanth Kumar, G.; Venkata Nagesh, B.; et al. (2023) (context) — Cited for the breadth of transaction types and the inherent variability of streaming financial data that detectors must absorb. [Sec. 2, p. 4]

---

Conversion: [`A--Huang-2025_marked.md`](../../literature/paper-markdowns/A--Huang-2025_marked.md)