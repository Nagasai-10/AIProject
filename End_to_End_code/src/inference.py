from __future__ import annotations  # Enables postponed evaluation of type annotations

from dataclasses import dataclass  # Used to create structured data classes
from typing import Dict, Any, List, Tuple  # Type hints for dictionaries, lists, and tuples

import torch  # PyTorch library for model loading and inference
from PIL import Image  # Image handling library

from .config import load_artifacts  # Loads model artifacts such as labels, config, and checkpoint path
from .model_factory import build_model  # Builds the selected model architecture
from .preprocessing import build_eval_transform, denorm_transform, ensure_pil_rgb  # Image preprocessing utilities
from .formatting import humanize_label, healthy_status  # Converts labels into readable format and health status
from .explainability import GradCAM, get_last_conv, overlay_cam_on_image  # Grad-CAM explainability utilities


# Stores the prediction output in a structured format
@dataclass
class PredictionResult:
    raw_class: str  # Original class label from the model
    display_class: str  # Human-readable class label
    confidence: float  # Prediction confidence score
    healthy_flag: str  # Indicates whether the plant is healthy or diseased
    top5: List[Tuple[str, float]]  # Top 5 predicted classes with confidence scores


# Creates a visual badge text based on plant health status
def health_badge_text(healthy_flag: str) -> str:
    return f"🟢 {healthy_flag}" if healthy_flag.lower() == "healthy" else f"🟠 {healthy_flag}"


# Main service class for plant disease prediction and explainability
class PlantDiseaseService:
    def __init__(self, artifact_dir: str = "artifacts"):
        # Select GPU if available, otherwise use CPU
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Load artifact bundle containing model checkpoint, labels, and config
        self.bundle = load_artifacts(artifact_dir)

        # Build model using the number of classes and selected architecture
        self.model = build_model(
            num_classes=self.bundle.num_classes,
            use_efficientnet=self.bundle.use_efficientnet,
        ).to(self.device)

        # Check whether trained model checkpoint exists
        if not self.bundle.checkpoint_path.exists():
            raise FileNotFoundError(
                f"Checkpoint not found: {self.bundle.checkpoint_path}. "
                "Copy best_model.pt from Kaggle into artifacts/."
            )

        # Load trained model weights
        state_dict = torch.load(self.bundle.checkpoint_path, map_location=self.device)
        self.model.load_state_dict(state_dict)

        # Set model to evaluation mode
        self.model.eval()

        # Build image preprocessing transform for inference
        self.transform = build_eval_transform(self.bundle.img_size)

        # Transform used to convert normalized tensor back to image format
        self.denorm = denorm_transform()

        # Initialize Grad-CAM using the last convolution layer of the model
        self.gradcam = GradCAM(self.model, get_last_conv(self.model))

    # Performs prediction and returns structured prediction result
    def predict(self, image) -> PredictionResult:
        # Ensure input image is a valid RGB PIL image
        pil_image = ensure_pil_rgb(image)

        # Apply preprocessing and add batch dimension
        tensor = self.transform(pil_image).unsqueeze(0).to(self.device)

        # Run inference without gradient calculation
        with torch.no_grad():
            logits = self.model(tensor)
            probs = torch.softmax(logits, dim=1).squeeze()

        # Get top 5 predicted classes
        top_probs, top_idxs = probs.topk(5)

        # Prepare top 5 predictions in readable format
        top5: List[Tuple[str, float]] = []
        for prob, idx in zip(top_probs.tolist(), top_idxs.tolist()):
            raw_label = self.bundle.labels[idx]
            top5.append((humanize_label(raw_label), float(prob)))

        # Get highest confidence class
        raw_class = self.bundle.labels[top_idxs[0].item()]

        # Return final prediction result
        return PredictionResult(
            raw_class=raw_class,
            display_class=humanize_label(raw_class),
            confidence=float(top_probs[0].item()),
            healthy_flag=healthy_status(raw_class),
            top5=top5,
        )

    # Performs prediction and also generates Grad-CAM explainability output
    def predict_with_explainability(self, image) -> Dict[str, Any]:
        # Ensure input image is converted to RGB PIL format
        pil_image = ensure_pil_rgb(image)

        # Preprocess image and move tensor to selected device
        tensor = self.transform(pil_image).unsqueeze(0).to(self.device)

        # Run model inference
        with torch.no_grad():
            logits = self.model(tensor)
            probs = torch.softmax(logits, dim=1).squeeze()

        # Extract top 5 prediction probabilities and indices
        top_probs, top_idxs = probs.topk(5)

        # Get predicted class index
        pred_idx = int(top_idxs[0].item())

        # Get raw and display class names
        raw_class = self.bundle.labels[pred_idx]
        display_class = humanize_label(raw_class)

        # Get confidence and health status
        confidence = float(top_probs[0].item())
        healthy_flag = healthy_status(raw_class)

        # Store top 5 predictions for table and dictionary output
        top5_table: List[List[str]] = []
        top5_dict: Dict[str, float] = {}

        # Format top 5 predictions
        for prob, idx in zip(top_probs.tolist(), top_idxs.tolist()):
            label = humanize_label(self.bundle.labels[idx])
            pct = f"{float(prob) * 100:.2f}%"
            top5_table.append([label, pct])
            top5_dict[label] = round(float(prob), 4)

        # Generate Grad-CAM heatmap for predicted class
        cam = self.gradcam(tensor, class_idx=pred_idx)

        # Convert tensor back to image format for overlay generation
        image_np = self.denorm(tensor.squeeze(0).cpu()).permute(1, 2, 0).clamp(0, 1).numpy()

        # Overlay Grad-CAM heatmap on original image
        overlay = overlay_cam_on_image(image_np, cam, self.bundle.img_size)

        # Prepare complete prediction summary
        summary = {
            "raw_class": raw_class,
            "display_class": display_class,
            "confidence": confidence,
            "confidence_pct": f"{confidence * 100:.2f}%",
            "healthy_flag": healthy_flag,
            "health_badge": health_badge_text(healthy_flag),
            "top5": top5_dict,
            "top5_table": top5_table,
            "overlay": overlay,
            "metrics": self.bundle.metrics if hasattr(self.bundle, "metrics") else {},
            "model_name": "EfficientNet-B2" if self.bundle.use_efficientnet else "ResNet-50",
            "num_classes": self.bundle.num_classes,
        }

        # Return prediction summary with explainability output
        return summary