# Validation of Automated Scores vs Existing Annotations

**Caveat:** the annotations (`topic_tags` / `topic_relevance` in the `_summarized.json`
files) were AI-generated under the **old** topic taxonomy (1.A-14.C) before the thesis
overhaul. They are a sanity check only — not ground truth. Use them to confirm the
automated scorer points in the same direction, then re-calibrate thresholds with judgment.

- Papers with at least one `medium`/`high` annotated topic: **0** / 91
- Point-biserial correlation (annotated med/high vs best combined score): **nan**
- Point-biserial correlation (annotated high vs best combined score): **nan**

Confusion vs `supporting_min=0.3` threshold (positive = automated relevance >= threshold):

| | annotated relevant | annotated not |
|---|---|---|
| automated >= thr | 0 (TP) | 89 (FP) |
| automated < thr  | 0 (FN) | 2 (TN) |

- Sensitivity (recall of annotated-relevant): **nan**
- Specificity: **0.022**
- Precision: **0.000**
- F1: **nan**

> If sensitivity is very low, many annotated-relevant papers fall below the threshold:
> lower `tiers.supporting_min` in config/modules.yaml. If specificity is very low,
> the threshold is too permissive. Adjust in config and re-run `scripts/score.py` only.