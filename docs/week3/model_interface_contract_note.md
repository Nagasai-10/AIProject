# Week 3 Model Interface Contract Note

## Context
Architecture decisions are only useful if the model has a clear interface contract. Week 3 is the right time to define what the model will later expect as input and what it must provide as output.

## Week 3 objective
The objective of this note is to define the interface assumptions that connect the model path to evaluation and deployment.

## Planned input contract
The baseline model path assumes:
- 224 × 224 RGB image input
- stable class mapping
- preprocessing consistency across environments
- compatibility with transfer-learning backbones

## Planned output contract
The model path should later support:
- one predicted class label
- confidence score
- top-k ranked alternatives
- explainability-friendly visual support

## Why this matters
A clear model interface contract improves reproducibility. It also makes it easier to align:
- the training stream
- the evaluation stream
- the deployed app
- the final demo narrative

## Week 4 handoff direction
In Week 4, this interface contract should guide the first implementation-ready baseline tasks and the packaging of outputs for evaluation and deployment.

## Summary
This Week 3 note defines the model interface contract so that architecture planning remains consistent across training, evaluation, and deployment.
