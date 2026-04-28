from __future__ import annotations  # Enables postponed evaluation of type annotations

from PIL import Image  # Used for image handling and conversions
from torchvision import transforms  # Provides image preprocessing utilities


# Builds the evaluation (inference) transformation pipeline
def build_eval_transform(img_size: int = 224):
    return transforms.Compose([
        # Resize image slightly larger than target size (common practice for center cropping)
        transforms.Resize(int(img_size * 1.14)),

        # Crop the center region to match the model input size
        transforms.CenterCrop(img_size),

        # Convert image to PyTorch tensor (scales pixel values to [0,1])
        transforms.ToTensor(),

        # Normalize using ImageNet mean and standard deviation
        # This is required because the model was trained on ImageNet-like data
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ])


# Builds a transformation to reverse normalization (useful for visualization)
def denorm_transform():
    return transforms.Compose([
        # Reverse standard deviation scaling
        transforms.Normalize(mean=[0.0, 0.0, 0.0], std=[1/0.229, 1/0.224, 1/0.225]),

        # Reverse mean normalization
        transforms.Normalize(mean=[-0.485, -0.456, -0.406], std=[1.0, 1.0, 1.0]),
    ])


# Ensures the input image is a valid RGB PIL Image
def ensure_pil_rgb(image) -> Image.Image:
    # If already a PIL Image, convert to RGB (ensures 3 channels)
    if isinstance(image, Image.Image):
        return image.convert("RGB")

    # If input is a NumPy array or other format, convert to PIL Image and then to RGB
    return Image.fromarray(image).convert("RGB")