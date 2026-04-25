# Week 4 Dataset Quality and Leakage Note

## Context
Operationalising the data pipeline in Week 4 requires explicit attention to quality control and leakage prevention.

## Week 4 objective
The objective of this note is to preserve a clear record of the main Week 4 risks affecting data reliability.

## Key risks

### inconsistent folder naming
This can destabilise class mapping across notebooks, scripts, and deployment outputs.

### hidden image-quality issues
Corrupt or unreadable files can silently damage training and evaluation if left untracked.

### weak split traceability
If split logic is not documented through manifests and metadata, later results become harder to defend.

### leakage through careless file handling
Poor control of similar or duplicated samples can inflate apparent model performance.

## Week 4 mitigation
- use canonical locations
- preserve metadata notes
- treat split control as a documented process
- keep quality concerns active in GitHub issue tracking

## Week 5 handoff direction
In Week 5, these controls should feed directly into final manifest generation and split-script implementation.

## Summary
This Week 4 note keeps leakage prevention and dataset quality visible so the data stream remains defensible.
