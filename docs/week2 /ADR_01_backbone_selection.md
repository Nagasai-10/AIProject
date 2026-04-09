# ADR-01: Backbone Selection

## Decision
EfficientNet-B2 is the intended primary backbone.
ResNet-50 is the fallback backbone.

## Context
The project requires a strong transfer-learning model for 23-class plant disease classification with a path to later deployment.

## Reasoning
EfficientNet-B2 offers a strong balance of accuracy and efficiency.
ResNet-50 is retained as a safe fallback if environment constraints arise.

## Deployment relevance
The final system should support:
- predicted class
- confidence score
- top-5 predictions
- explainability-friendly outputs
