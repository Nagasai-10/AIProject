# Week 4 Canonical File Structure Note

## Context
Week 4 requires the dataset stream to move from planning into operational reproducibility. This requires one canonical structure that all environments can trust.

## Week 4 objective
The objective of this note is to define one stable directory logic for manifests, metadata, and split-ready outputs.

## Proposed structure

```text
data/
├── raw/
├── interim/
├── processed/
├── manifests/
└── metadata/
```

## Role of each area

### raw
Stores the original dataset source as unchanged as possible.

### interim
Stores temporary audit outputs and working checks.

### processed
Stores later cleaned or split-ready outputs where needed.

### manifests
Stores train / validation / test manifest files, label mappings, and structured path records.

### metadata
Stores audit summaries, naming observations, and quality-control notes.

## Why this matters
A canonical structure reduces ambiguity across Kaggle, Colab, GitHub, VS Code, and deployment packaging. It also improves traceability because manifests and metadata remain visible instead of scattered across notebooks.

## Week 5 handoff direction
This structure should guide implemented split scripts and pipeline-ready directory logic in Week 5.

## Summary
This Week 4 note fixes the data layout into a reusable canonical form so later engineering work remains reproducible.
