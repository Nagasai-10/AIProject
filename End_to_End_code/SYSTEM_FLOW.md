# End-to-End System Flow

## 1. Training side (Kaggle only)

```text
PlantVillage Dataset
    ↓
Audit / EDA / duplicate checks
    ↓
Train / Val / Test manifests
    ↓
Transfer learning model training
    ↓
Evaluation + Grad-CAM + artifact export
    ↓
best_model.pt + labels.json + config.json + metrics.json
```

## 2. Inference side (VS Code / Local)

```text
Exported Kaggle artifacts
    ↓
Load model + labels + config
    ↓
User uploads image
    ↓
Preprocess image
    ↓
Run inference
    ↓
Generate:
- predicted class
- confidence
- top-5 predictions
- healthy/diseased tag
- Grad-CAM overlay
```

## 3. Deployment side (Hugging Face Spaces)

```text
Same codebase
    ↓
Gradio UI
    ↓
Public user interaction
    ↓
Prediction + explainability + disclaimer
```

## 4. Engineering principle

- **Kaggle** = training and export
- **VS Code** = local UI testing and packaging
- **Hugging Face Spaces** = final user experience
- **No retraining in VS Code**
