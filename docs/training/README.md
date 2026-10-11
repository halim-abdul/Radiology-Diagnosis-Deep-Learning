# Training and evaluation

The training loop emits uncalibrated logits; apply sigmoid for probabilities and calibrate on held-out validation only. Report AUROC, average precision, confidence intervals, sensitivity, specificity, data prevalence, operating thresholds, external validation, and per-site / scanner / demographic strata where legally and ethically permissible. Clinical utility is not established by smoke tests.
