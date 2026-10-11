# Evaluation protocol

1. Document modality, institution, timeframe, inclusion/exclusion, scanner, label provenance and preprocessing.
2. Split by patient, and where needed by hospital and time; lock the test set.
3. Train only on train split; tune hyperparameters and thresholds on validation.
4. Evaluate classification with AUROC/AUPRC and uncertainty; segmentation with Dice/IoU and physical-space distances.
5. Validate probability calibration, failure modes and distribution shift on external data.
6. Report confidence intervals based on grouped/cluster-aware bootstraps; do not fabricate results.
7. Perform reader studies before describing clinical effectiveness.
