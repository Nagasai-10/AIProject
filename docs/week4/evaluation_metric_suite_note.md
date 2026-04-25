# Week 4 Evaluation Metric Suite Note

## Context
Week 4 requires the evaluation stream to become operational before the first baseline experiments dominate attention.

## Week 4 objective
The objective of this note is to freeze the core metric suite that later experiments must generate.

## Planned metric suite
- overall accuracy
- macro precision
- macro recall
- macro F1
- per-class performance
- confusion-based interpretation

## Why this matters
A single accuracy figure is not enough for a 23-class problem. A richer suite is needed to expose minority-class weakness, confusion pairs, and imbalance effects.

## Week 5 handoff direction
In Week 5, this metric suite should drive the structure of saved predictions, result tables, and evaluation exports.

## Summary
This Week 4 note operationalises the evaluation baseline so later experiments are measured defensibly.
