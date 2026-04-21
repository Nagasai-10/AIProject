
# Week 3 Dataset Audit Scope Note

## Context
Week 3 marks the transition from broad planning into data-readiness execution. At this stage, dataset work should not remain at the level of general EDA only. It must begin producing structured, traceable outputs that later model, evaluation, and ethics streams can rely on.

## Week 3 objective
The objective of this note is to define the scope of the Week 3 dataset audit and make clear what checks must be completed before the first controlled engineering runs begin.

## Audit scope
The Week 3 dataset audit should cover the following areas:

### 1. Class and folder verification
- confirm the expected class folders are present
- verify that folder names are consistent with the agreed label mapping
- identify any naming irregularities that could later affect scripts, reports, or inference outputs

### 2. File-level inspection
- identify missing or unreadable files
- detect corrupted images where possible
- note unsupported extensions or unusual file patterns
- record any obvious anomalies that could affect preprocessing

### 3. Basic structure readiness
- confirm that the raw dataset is arranged in a way that supports reproducible split creation
- define how raw files, manifests, and later split outputs should be tracked
- ensure that the data stream can hand off cleanly into preprocessing and modeling work

### 4. Split-readiness checks
- review whether the dataset is ready for train / validation / test planning
- identify any class-level concerns that could affect split quality
- note anything that may increase leakage risk or reduce traceability

## Why this matters
Dataset work in Week 3 is not only about inspection. It is about making the data stream operational. If audit outputs remain informal or undocumented, later modeling and evaluation work will rely on assumptions instead of audited inputs. That weakens both reproducibility and later academic reporting.

## Links to later work
This note should support:
- canonical file-structure design
- split-manifest creation
- preprocessing assumptions
- evaluation readiness
- ethics and bias review
- GitHub issue tracking

## Week 4 handoff direction
In Week 4, this audit scope should translate into practical outputs such as dataset manifests, split scripts, and pipeline-ready directory logic.

## Summary
This Week 3 note formalises the scope of dataset auditing so that the data stream becomes a controlled and traceable part of the project rather than an informal preparation step.
