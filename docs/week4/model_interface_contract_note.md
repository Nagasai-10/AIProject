# Week 4 Model Interface Contract Note

## Context
The baseline model needs a clear interface contract so that training, evaluation, UI, and deployment remain aligned.

## Week 4 objective
The objective of this note is to freeze the essential input and output assumptions for the baseline system.

## Input contract
- 224 × 224 RGB image input
- stable label mapping
- preprocessing consistency across environments
- compatibility with the selected transfer-learning backbone

## Output contract
The baseline should later support:
- predicted class
- confidence score
- top-k ranked alternatives
- explainability-friendly visual support

## Why this matters
Without a clear contract, implementation fragments across streams. This note keeps the model path aligned to deployment and demo needs.

## Week 5 handoff direction
In Week 5, this contract should guide baseline implementation, inference formatting, and deployment-facing design.

## Summary
This Week 4 note defines the model interface in a form that supports consistent implementation and deployment.
