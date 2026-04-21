
# Week 3 Architecture Refinement Note

## Context
Week 3 architecture planning should now move beyond a broad CNN direction and become more tightly aligned with the audited dataset assumptions and the practical deployment workflow.

## Week 3 objective
The objective of this note is to refine the model path so that architecture decisions remain realistic, traceable, and implementation-ready.

## Core Week 3 architecture direction
The project will continue to treat transfer learning as the main strategy for the 23-class PlantVillage classification task. However, in Week 3 the model path is refined further by connecting it more clearly to:
- audited dataset assumptions
- consistent class mapping
- stable input sizing
- inference output requirements
- later deployment needs

## Architecture refinement points

### 1. Keep the model downstream of audited data
Architecture decisions should not drift ahead of data-readiness work. The model path should assume that class labels, folder naming, and preprocessing expectations are stable.

### 2. Preserve one primary backbone and one fallback
The intended primary path remains EfficientNet-B2, while ResNet-50 remains the fallback. This avoids architecture sprawl.

### 3. Fix the input contract
The model design should assume a stable 224 × 224 RGB input standard for baseline implementation.

### 4. Remain deployment-aware
The architecture discussion should consider what the deployed system must later return:
- predicted class
- confidence
- top-k outputs
- explainability-friendly output

## Why this matters
This refinement helps ensure that Week 4 implementation is based on clear assumptions instead of repeated architecture redefinition.

## Week 4 handoff direction
In Week 4, these decisions should translate into baseline model-building tasks and implementation notes.

## Summary
This Week 3 note refines the architecture path so that it stays aligned with audited data assumptions, compute realism, and later deployment requirements.
