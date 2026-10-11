# Modality-specific normalization

## Scientific motivation

MRI intensity scales vary by scanner and sequence; CT values can be physical Hounsfield Units when properly decoded.

## Mathematical or methodological point

Population-wide normalization statistics must be estimated on training data only.

## Experimental design

Track modality-specific windows and distinguish display from model preprocessing. When designing a benchmark, document the source population, dataset provenance, validation design, key assumptions, and whether this hypothesis has actually been tested.

## Status and interpretation

This is a **research handbook note**, not a completed experiment, clinical result, or evidence of diagnostic validity. Revisit the relevant method, cite primary research sources in a formal manuscript, and keep patient data outside Git.
