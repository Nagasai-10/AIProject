# Week 3 Train Validation Test and Leakage Note

## Context
Evaluation only becomes trustworthy if it is supported by defensible split logic and leakage-aware data handling.

## Week 3 objective
The objective of this note is to make split discipline and leakage awareness visible during the planning-to-data transition.

## Key points
- training data should support fitting
- validation data should support tuning and checkpoint decisions
- test data should remain held out for final evaluation
- leakage awareness should remain active from the data stage onward

## Why this matters
If split logic is weak, later metrics may appear stronger than they really are. This note keeps evaluation tied to sound data practice.

## Week 4 handoff direction
In Week 4, split logic and leakage checks should begin feeding directly into manifests, logging, and metrics workflows.

## Summary
This Week 3 note keeps evaluation defensible by linking it to disciplined split planning and leakage prevention.
