# Smart Crop Health Monitoring — LeafGuard AI

**LeafGuard AI** is a Gradio-based plant leaf disease screening application that uses a trained deep-learning model to classify crop leaf images and return confidence-ranked predictions.

The project is designed as an **inference and deployment codebase**. Model training is completed separately in Kaggle, and the exported model artifacts are reused locally in VS Code and on Hugging Face Spaces.

## Live Demo

Try the deployed application here:

[LeafGuard AI on Hugging Face Spaces](https://huggingface.co/spaces/Ravichakka/LeafGuard_AI)

## Project Overview

The application allows users to upload a plant leaf image and receive:

- Predicted crop disease / healthy class
- Confidence score for the top prediction
- Top-5 confidence-ranked alternatives
- Crop name and health status
- Smart interpretation for decision support
- Responsible-use guidance for safe agricultural decision-making

The current interface supports **23 plant disease / healthy classes** across crops such as **Apple, Corn/Maize, Pepper Bell, Potato, and Tomato**.

## Application Screenshots

> Save your screenshots inside `docs/screenshots/` using the filenames below, then these images will render correctly in GitHub and Hugging Face README pages.

| No Prediction State | Apple Scab Prediction | Corn Leaf Blight Prediction |
|---|---|---|
| ![No prediction UI](docs/screenshots/no-prediction-state.png) | ![Apple scab prediction](docs/screenshots/apple-scab-prediction.png) | ![Corn leaf blight prediction](docs/screenshots/corn-leaf-blight-prediction.png) |

### UI Highlights

- Clean academic demo interface built with Gradio
- Image upload panel with drag-and-drop support
- Prediction dashboard with confidence badge
- Top-5 probability ranking for transparency
- Smart interpretation section for practical guidance
- Decision-support disclaimer to avoid unsafe overreliance

## Example Predictions

The app can return predictions like:

| Uploaded Leaf | Predicted Condition | Confidence |
|---|---:|---:|
| Apple leaf | Apple - Apple scab | ~90% |
| Corn/Maize leaf | Corn (maize) - Northern Leaf Blight | ~91% |

These values are examples from the deployed demo interface. Actual confidence scores may vary depending on the uploaded image quality, lighting, background, symptoms, and model checkpoint.

## Workflow

```text
Kaggle Notebook
  ├─ Dataset audit / EDA
  ├─ Cleaning / split manifests
  ├─ Training / evaluation / Grad-CAM experiments
  └─ Export artifacts
          ↓
Local VS Code App
  ├─ Load best_model.pt
  ├─ Load labels.json + config.json
  ├─ Run inference only
  ├─ Show prediction + confidence + top-5 probabilities
  └─ Validate user experience
          ↓
Hugging Face Spaces
  ├─ Same app.py
  ├─ Same src/ modules
  ├─ Same exported artifacts
  └─ Public Gradio deployment
```

## What This Repo Does

This repository focuses on **deployment-side inference**. It avoids retraining in VS Code or Hugging Face Spaces.

Training is handled in Kaggle, then the exported artifacts are copied into this project for:

1. Local inference testing
2. UI validation
3. Hugging Face Spaces deployment
4. Academic demonstration and decision-support use

## Required Kaggle Artifacts

Place the following files inside the `artifacts/` folder:

```text
artifacts/
├── best_model.pt
├── labels.json
├── config.json
└── metrics.json        # optional but recommended
```

Optional visual/export files:

```text
artifacts/
├── training_curves.png
├── confusion_matrix.png
├── per_class_accuracy.png
└── gradcam_samples.png
```

## Project Structure

```text
smart_crop_inference_project/
├── app.py
├── README.md
├── requirements.txt
├── SYSTEM_FLOW.md
├── launch_local.bat
├── artifacts/
│   ├── README.md
│   ├── best_model.pt
│   ├── labels.json
│   ├── config.json
│   └── metrics.json
├── docs/
│   └── screenshots/
│       ├── no-prediction-state.png
│       ├── apple-scab-prediction.png
│       └── corn-leaf-blight-prediction.png
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

## Local Setup in VS Code

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the environment

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

### 4. Add Kaggle exports

Copy the required files into the `artifacts/` folder:

```text
best_model.pt
labels.json
config.json
```

### 5. Verify artifacts

```bash
python scripts/verify_artifacts.py
```

### 6. Run the app locally

```bash
python app.py
```

After running the command, open the local Gradio URL shown in the terminal.

## Hugging Face Spaces Deployment

This project is deployed as a **Gradio Space**.

### Deployment Steps

1. Create a new Hugging Face Space.
2. Select **Gradio** as the Space SDK.
3. Upload or push the following files/folders:
   - `app.py`
   - `requirements.txt`
   - `src/`
   - `artifacts/`
   - `README.md`
4. Confirm that these files exist:
   - `artifacts/best_model.pt`
   - `artifacts/labels.json`
   - `artifacts/config.json`
5. Commit the files and allow the Space to rebuild.
6. Open the Space app and test prediction using sample leaf images.

## UI Output Details

When a user uploads a leaf image and clicks **Analyze Leaf**, the app displays:

- **Predicted condition**: most likely disease or healthy class
- **Confidence score**: probability for the predicted class
- **Crop**: detected crop category
- **Health status**: healthy or disease detected
- **Top-5 prediction probabilities**: confidence-ranked alternatives
- **Smart interpretation**: safe, practical explanation for the prediction

## Best Image Tips

For better predictions, upload images with:

- One clear leaf in the image
- Good lighting
- Visible symptoms
- Minimal background clutter
- No heavy shadows
- No multiple overlapping leaves

## Important Design Rule

This repo is for **inference and user experience only**.

Do not retrain the model inside VS Code or Hugging Face Spaces. Training should remain in Kaggle, and only the exported artifacts should be used here.

## Suggested Kaggle Export Checklist

At the end of training, export:

- `best_model.pt`
- `labels.json`
- `config.json`
- `metrics.json`
- Training curves and evaluation plots, if available
- Grad-CAM samples, if available

Then place those files inside the `artifacts/` folder before running or deploying the app.

## Responsible Use Note

LeafGuard AI is intended for **academic demonstration and agricultural decision support only**.

The predictions should not replace expert agronomic advice. Before applying treatment in the field, users should confirm the disease with an agriculture expert, local extension officer, or qualified crop advisor.
