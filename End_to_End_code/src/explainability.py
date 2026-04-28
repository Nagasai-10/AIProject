from __future__ import annotations  # Enables postponed evaluation of type hints

from typing import Optional  # Used for optional type annotations
import numpy as np  # Numerical operations
import torch  # PyTorch core library
import torch.nn as nn  # Neural network modules
from PIL import Image  # Image processing
import matplotlib.pyplot as plt  # For colormap visualization


# Grad-CAM implementation for visualizing model attention
class GradCAM:
    def __init__(self, model: nn.Module, target_layer: nn.Module):
        self.model = model  # The trained model
        self.gradients: Optional[torch.Tensor] = None  # Stores gradients of target layer
        self.activations: Optional[torch.Tensor] = None  # Stores feature maps (activations)

        # Register hooks to capture forward activations and backward gradients
        target_layer.register_forward_hook(self._save_activations)
        target_layer.register_full_backward_hook(self._save_gradients)

    # Hook function to store activations during forward pass
    def _save_activations(self, _, __, output):
        self.activations = output.detach()

    # Hook function to store gradients during backward pass
    def _save_gradients(self, _, __, grad_output):
        self.gradients = grad_output[0].detach()

    # Main function to compute Grad-CAM heatmap
    def __call__(self, input_tensor: torch.Tensor, class_idx: Optional[int] = None) -> np.ndarray:
        self.model.eval()  # Set model to evaluation mode

        # Forward pass
        output = self.model(input_tensor)

        # If no class specified, use predicted class
        if class_idx is None:
            class_idx = int(output.argmax(dim=1).item())

        # Backward pass for selected class
        self.model.zero_grad()
        output[0, class_idx].backward()

        # Compute weights by global average pooling of gradients
        weights = self.gradients.mean(dim=(2, 3), keepdim=True)

        # Compute weighted combination of activations
        cam = (weights * self.activations).sum(dim=1).squeeze()

        # Apply ReLU and normalize heatmap
        cam = torch.relu(cam).detach().cpu().numpy()
        return (cam - cam.min()) / (cam.max() - cam.min() + 1e-8)


# Utility function to get the last convolutional layer from the model
def get_last_conv(model: nn.Module) -> nn.Module:
    last_conv = None

    # Iterate through all modules to find the last Conv2d layer
    for module in model.modules():
        if isinstance(module, nn.Conv2d):
            last_conv = module

    # Raise error if no convolution layer is found
    if last_conv is None:
        raise ValueError("No convolution layer found for Grad-CAM.")

    return last_conv


# Function to overlay Grad-CAM heatmap on the original image
def overlay_cam_on_image(image_np: np.ndarray, cam: np.ndarray, img_size: int = 224) -> Image.Image:
    # Resize CAM to match image size
    cam_resized = np.array(
        Image.fromarray((cam * 255).astype(np.uint8)).resize((img_size, img_size), Image.BILINEAR)
    ) / 255.0

    # Apply jet colormap to create heatmap
    heatmap = plt.cm.jet(cam_resized)[:, :, :3]

    # Blend original image and heatmap
    overlay = 0.5 * image_np + 0.5 * heatmap
    overlay = np.clip(overlay, 0, 1)  # Ensure pixel values are valid

    # Convert to image format
    return Image.fromarray((overlay * 255).astype(np.uint8))