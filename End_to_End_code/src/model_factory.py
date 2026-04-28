from __future__ import annotations  # Enables postponed evaluation of type hints

import torch.nn as nn  # Neural network modules
from torchvision import models  # Pretrained models from torchvision


# Function to build model architecture dynamically
def build_model(num_classes: int, use_efficientnet: bool = True) -> nn.Module:

    # If EfficientNet is preferred
    if use_efficientnet:
        try:
            # Import EfficientNet-B2 model and its pretrained weights
            from torchvision.models import efficientnet_b2, EfficientNet_B2_Weights

            # Load pretrained EfficientNet-B2 model
            model = efficientnet_b2(weights=EfficientNet_B2_Weights.DEFAULT)

            # Get input feature size of classifier layer
            in_features = model.classifier[1].in_features

            # Replace classifier head with custom layers for our number of classes
            model.classifier = nn.Sequential(
                nn.Dropout(0.3),  # Dropout for regularization
                nn.Linear(in_features, num_classes),  # Final classification layer
            )

            return model  # Return modified EfficientNet model

        except Exception:
            # If EfficientNet import or loading fails, fallback to ResNet
            pass

    # Fallback model: ResNet-50
    model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)

    # Replace fully connected layer with custom classifier
    model.fc = nn.Sequential(
        nn.Dropout(0.3),  # Dropout for regularization
        nn.Linear(model.fc.in_features, num_classes),  # Final classification layer
    )

    return model  # Return modified ResNet model