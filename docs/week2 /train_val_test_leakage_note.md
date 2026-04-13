# Week 2 Train Validation Test and Leakage Note

Evaluation must be supported by a proper train, validation, and test separation.

Key points:
- train data is used for model fitting
- validation data is used for tuning and checkpoint decisions
- test data is reserved for final evaluation
- leakage risks must be considered early

Reasoning:
Without clear split planning, later metrics may appear stronger than they really are. This note keeps evaluation tied to defensible data practice.
