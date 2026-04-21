
# Week 3 Dataset Quality and Leakage Note

## Context
Week 3 data-readiness planning must also address quality-control risks. If these are ignored early, later training and evaluation outputs may be difficult to trust.

## Week 3 objective
The objective of this note is to record the main Week 3 risks related to dataset quality and leakage.

## Key risks identified

### 1. Inconsistent folder naming
If folder names are inconsistent or poorly controlled, class mapping can become unstable across notebooks, scripts, and deployment outputs.

### 2. Hidden data-quality problems
Unreadable files, corrupted images, or unusual extensions may silently affect the pipeline if they are not checked and logged.

### 3. Weak split traceability
If split logic is not recorded through manifests or metadata, later evaluation becomes harder to justify.

### 4. Leakage through careless file handling
If similar or duplicated images are handled poorly, the final evaluation may appear stronger than it really is.

## Week 3 mitigation direction
The Week 3 response is to:
- define canonical file locations
- record dataset observations through notes and manifests
- treat split planning as a documented process
- keep issue tracking active for data-quality concerns

## Why this matters
These controls help ensure that later metrics, architecture decisions, and ethical analysis are grounded in a reliable data stream rather than hidden assumptions.

## Week 4 handoff direction
In Week 4, these concerns should inform split scripts, manifest generation, and audit-linked quality checks.

## Summary
This Week 3 note keeps data-quality and leakage prevention visible so that the pipeline remains defensible and traceable.
