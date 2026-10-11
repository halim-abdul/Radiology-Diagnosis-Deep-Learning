# Augmentation validity

## Scientific motivation

Artificial rotations, flips and crops must preserve the intended label and anatomy.

## Mathematical or methodological point

Random left-right flips can invert laterality and invalidate many radiology labels.

## Experimental design

Test each transform against clinical annotation semantics. When designing a benchmark, document the source population, dataset provenance, validation design, key assumptions, and whether this hypothesis has actually been tested.

## Status and interpretation

This is a **research handbook note**, not a completed experiment, clinical result, or evidence of diagnostic validity. Revisit the relevant method, cite primary research sources in a formal manuscript, and keep patient data outside Git.
