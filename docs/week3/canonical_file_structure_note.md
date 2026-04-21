
# Week 3 Canonical File Structure Note

## Context
Week 3 data planning requires a stable and reproducible file structure. Without one canonical layout, later scripts, manifests, checkpoints, and evaluation outputs can become inconsistent across Kaggle, Colab, GitHub, and local VS Code development.

## Week 3 objective
The objective of this note is to define one clear and reusable directory logic for dataset handling and split-output organisation.

## Proposed canonical structure

```text
data/
├── raw/
├── interim/
├── processed/
├── manifests/
└── metadata/
