from pathlib import Path
import json

artifact_dir = Path("artifacts")
required = ["best_model.pt", "labels.json", "config.json"]

print("Checking artifacts in:", artifact_dir.resolve())
missing = [name for name in required if not (artifact_dir / name).exists()]

if missing:
    print("Missing required files:")
    for item in missing:
        print(" -", item)
else:
    print("All required files are present.")

for optional in ["metrics.json", "training_curves.png", "confusion_matrix.png", "per_class_accuracy.png", "gradcam_samples.png"]:
    if (artifact_dir / optional).exists():
        print("Optional artifact found:", optional)

labels_file = artifact_dir / "labels.json"
if labels_file.exists():
    with open(labels_file, "r", encoding="utf-8") as f:
        labels = json.load(f)
    print("Labels count:", len(labels))
