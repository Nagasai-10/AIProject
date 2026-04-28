from __future__ import annotations  # Enables postponed evaluation of type annotations (useful for forward references)

import json  # Used for reading configuration and label files
from dataclasses import dataclass  # Used to define a simple class for storing artifact-related data
from pathlib import Path  # Provides an object-oriented way to handle file paths
from typing import List, Dict, Any  # Type hinting for better code clarity

from .constants import DEFAULT_LABELS  # Default labels used if no labels file is found


# Dataclass to store all artifact-related information in a structured way
@dataclass
class ArtifactBundle:
    artifact_dir: Path  # Directory where artifacts are stored
    checkpoint_path: Path  # Path to the trained model file
    labels: List[str]  # List of class labels
    config: Dict[str, Any]  # Configuration dictionary (e.g., image size, model type)

    # Returns image size from config (default is 224 if not specified)
    @property
    def img_size(self) -> int:
        return int(self.config.get("img_size", 224))

    # Returns whether EfficientNet is used (default True)
    @property
    def use_efficientnet(self) -> bool:
        return bool(self.config.get("use_efficientnet", True))

    # Returns number of classes based on labels
    @property
    def num_classes(self) -> int:
        return len(self.labels)


# Function to load model artifacts (checkpoint, labels, config)
def load_artifacts(artifact_dir: str | Path = "artifacts") -> ArtifactBundle:
    artifact_dir = Path(artifact_dir)  # Convert input to Path object

    # Define paths for required files
    checkpoint_path = artifact_dir / "best_model.pt"
    labels_path = artifact_dir / "labels.json"
    config_path = artifact_dir / "config.json"

    # Load labels (use default if file does not exist)
    labels = DEFAULT_LABELS
    if labels_path.exists():
        with open(labels_path, "r", encoding="utf-8") as f:
            labels = json.load(f)

    # Default configuration values
    config: Dict[str, Any] = {"img_size": 224, "use_efficientnet": True}

    # Load config file if available and update defaults
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config.update(json.load(f))

    # Return structured artifact bundle
    return ArtifactBundle(
        artifact_dir=artifact_dir,
        checkpoint_path=checkpoint_path,
        labels=labels,
        config=config,
    )