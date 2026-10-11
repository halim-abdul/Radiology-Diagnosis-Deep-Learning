# Ablation design

## Scientific motivation

Architecture components must be evaluated against proper controls under comparable compute budgets.

## Concrete evaluation design

Hold data split fixed and repeat across random seeds. Compare with appropriate baselines. Describe the data-generating mechanism, clinical label semantics, statistical unit of analysis and evaluation conditions rather than treating every scan as independent.

## Research interpretation

Log model versions, random seeds and provenance. Analyze error cases, assumptions and possible distribution shift; perform external replication if evidence supports further investigation. **This is a research handbook entry—not completed experimental evidence or medical advice.**
