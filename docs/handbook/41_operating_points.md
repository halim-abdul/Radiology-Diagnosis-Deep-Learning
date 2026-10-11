# Operating threshold selection

## Scientific motivation

Sensitivity and specificity reflect an operating point that must be prespecified on validation data.

## Concrete evaluation design

Never tune thresholds against the final test set. Compare with appropriate baselines. Describe the data-generating mechanism, clinical label semantics, statistical unit of analysis and evaluation conditions rather than treating every scan as independent.

## Research interpretation

Log model versions, random seeds and provenance. Analyze error cases, assumptions and possible distribution shift; perform external replication if evidence supports further investigation. **This is a research handbook entry—not completed experimental evidence or medical advice.**
