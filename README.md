# Smart Crop Health Monitoring — Inference + UI + Hugging Face Flow

This project is the **deployment-side codebase** for your trained plant disease model.

You **train in Kaggle**, then **reuse the trained checkpoint in VS Code** for local UI testing and the **same app** can be pushed to **Hugging Face Spaces** for user-facing deployment.

## Workflow

```text
Kaggle Notebook
  ├─ Dataset audit / EDA
  ├─ Cleaning / split manifests
  ├─ Training / evaluation / Grad-CAM
  └─ Export artifacts
          ↓
Local VS Code App
  ├─ Load best_model.pt
  ├─ Load labels.json + config.json
  ├─ Run inference only
  ├─ Show class + confidence + top-5 + Grad-CAM
  └─ Validate user experience
          ↓
Hugging Face Spaces
  ├─ Same app.py
  ├─ Same src/ modules
  └─ Same exported artifacts
```

## What this repo does

This repo is designed to **avoid retraining in VS Code**.  
VS Code and Hugging Face both use the **trained artifacts exported from Kaggle**.

## Required artifacts from Kaggle

Place these files into the `artifacts/` folder:

- `best_model.pt`
- `labels.json`
- `config.json`
- `metrics.json` *(optional but recommended)*

Optional visual/export files:
- `training_curves.png`
- `confusion_matrix.png`
- `per_class_accuracy.png`
- `gradcam_samples.png`

## Project structure

```text
smart_crop_inference_project/
├── app.py
├── README.md
├── requirements.txt
├── SYSTEM_FLOW.md
├── launch_local.bat
├── artifacts/
│   ├── README.md
│   └── best_model.pt / labels.json / config.json / metrics.json
├── src/
│   ├── __init__.py
│   ├── constants.py
│   ├── config.py
│   ├── model_factory.py
│   ├── preprocessing.py
│   ├── formatting.py
│   ├── explainability.py
│   └── inference.py
└── scripts/
    └── verify_artifacts.py
```

## Local setup in VS Code

### 1. Create environment
```bash
python -m venv .venv
```

### 2. Activate environment

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Put Kaggle exports into `artifacts/`
Required:
- `best_model.pt`
- `labels.json`
- `config.json`

### 5. Verify artifacts
```bash
python scripts/verify_artifacts.py
```

### 6. Run the UI
```bash
python app.py
```

## Hugging Face Spaces deployment

Use **Gradio** with **Python**.

### Recommended steps
1. Create a new Hugging Face Space
2. Choose **Gradio**
3. Upload:
   - `app.py`
   - `requirements.txt`
   - `src/`
   - `artifacts/`
4. Make sure `artifacts/best_model.pt`, `labels.json`, and `config.json` are present
5. Commit and let the Space build

## UI outputs

The app shows:
- Predicted class
- Human-readable label
- Confidence score
- Top-5 probabilities
- Healthy / Diseased flag
- Grad-CAM overlay
- Responsible-use disclaimer

## Important design rule

This repo is for **inference and user experience**, not model training.  
Training remains in **Kaggle**.

## Suggested Kaggle export checklist

At the end of training, save:
- `best_model.pt`
- `labels.json`
- `config.json`
- `metrics.json`

You can then download those files and place them into `artifacts/`.

## Responsible use note

This system is intended for **decision support only**.  
Predictions should not be treated as a replacement for expert agronomic advice.
