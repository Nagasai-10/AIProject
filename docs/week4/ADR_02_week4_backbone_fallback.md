# ADR-02 Week 4 Backbone and Fallback Note

## Decision
EfficientNet-B2 remains the primary backbone. ResNet-50 remains the controlled fallback.

## Context
Week 4 is a pipeline-operational phase, so the architecture should not branch into many competing paths. A single strong primary route with one fallback keeps the project stable.

## Reasoning
EfficientNet-B2 continues to offer a strong balance between feature quality and efficiency. ResNet-50 remains a reliable fallback if environment or compatibility constraints affect the primary route.

## Why this matters
This decision:
- reduces architecture sprawl
- preserves tutor-facing clarity
- supports deployment planning
- keeps Week 5 baseline work focused

## Week 5 handoff direction
In Week 5, the primary path should be implemented first, with the fallback retained only for controlled contingency use.

## Summary
This Week 4 ADR keeps the model strategy disciplined by freezing one primary backbone and one fallback pathway.
