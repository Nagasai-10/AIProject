# Week 4 Dataset Audit Scope Note

## Context
Week 4 marks the movement from Week 3 data-readiness planning into operational pipeline work. The goal is no longer broad inspection alone. The goal is to create durable, auditable outputs that later model, evaluation, and ethics streams can trust.

## Week 4 objective
The objective of this note is to formalise the Week 4 dataset audit scope so that the data stream becomes implementation-ready and traceable.

## Operational audit scope

### 1. Class and folder verification
- confirm that all expected class folders are present
- verify naming consistency against the agreed label set
- record any naming irregularities that could affect manifests, scripts, or deployment outputs

### 2. File-level quality checks
- identify corrupt or unreadable images
- note unsupported or inconsistent file extensions
- preserve a clear record of image-quality observations

### 3. Manifest-readiness checks
- ensure that raw files can be represented cleanly in train / validation / test manifests
- verify that paths are stable enough for later script consumption
- make sure later split generation remains auditable

### 4. Downstream handoff readiness
- confirm that audited data can be consumed by architecture, training, evaluation, and ethics streams without ambiguity
- keep metadata notes visible so that later scripts and reports use the same assumptions

## Why this matters
If Week 4 data work remains informal, later model and evaluation outputs will rely on weak assumptions. This note turns the audit into a controlled operational step rather than a notebook-only activity.

## Week 5 handoff direction
In Week 5, this audit scope should support finalised split scripts, dataset manifests, and pipeline-ready directory logic.

## Summary
This Week 4 note closes the audit stage by making class checks, quality checks, and downstream handoff rules explicit and reusable.
