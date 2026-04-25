# Week 4 Architecture Refinement Note

## Context
Week 4 architecture work moves from refinement into freezing the baseline direction. The aim is to preserve only the necessary decisions that support implementation.

## Week 4 objective
The objective of this note is to stabilise the model path against operational pipeline assumptions and later deployment needs.

## Week 4 architecture position
- transfer learning remains the core strategy
- EfficientNet-B2 remains the primary backbone
- ResNet-50 remains the fallback
- 224 × 224 input remains the baseline standard
- class mapping and output logic must stay consistent across training, evaluation, and deployment

## Why this matters
Week 4 should reduce architecture drift, not increase it. Freezing the necessary decisions now makes Week 5 implementation cleaner and more defensible.

## Week 5 handoff direction
In Week 5, these decisions should become baseline implementation tasks, classifier-head work, and issue-linked development steps.

## Summary
This Week 4 note stabilises the architecture path so it is ready for controlled baseline implementation.
