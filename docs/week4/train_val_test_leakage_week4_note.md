# Week 4 Train Validation Test and Leakage Note

## Context
Evaluation remains trustworthy only if split discipline and leakage awareness are treated as operational controls.

## Week 4 objective
The objective of this note is to keep split quality and leakage checks visible during the first baseline phase.

## Key requirements
- train data supports fitting
- validation data supports tuning and checkpoint decisions
- test data remains held out
- saved predictions should remain traceable
- class-distribution monitoring should remain active

## Why this matters
Weak split discipline can inflate apparent performance and weaken the credibility of public claims.

## Week 5 handoff direction
In Week 5, these rules should connect directly to saved-prediction hooks, manifests, and evaluation logging.

## Summary
This Week 4 note keeps evaluation tied to defensible data practice and leakage prevention.
