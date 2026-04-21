# ADR-02 Week 3 Backbone and Fallback Note

## Decision
EfficientNet-B2 remains the intended primary backbone for the project. ResNet-50 remains the controlled fallback path.

## Context
The project requires a strong transfer-learning model for 23-class leaf-image classification, but Week 3 planning must avoid introducing unnecessary architectural variation while data-readiness work is still active.

## Reasoning
EfficientNet-B2 remains attractive because it offers a strong balance between accuracy and efficiency. ResNet-50 remains the fallback because it is stable, well-supported, and practical if environment constraints affect implementation.

## Risk control value
This ADR is useful because it:
- reduces architecture drift
- preserves one clear primary path
- maintains a practical fallback
- helps keep tutor-facing planning defensible

## Deployment relevance
The chosen path must still support the later deployment requirements:
- class prediction
- confidence
- top-k output
- explainability-friendly visuals

## Summary
This ADR preserves a disciplined architecture strategy by keeping one strong primary backbone and one clear fallback pathway.
