from __future__ import annotations

from PIL import Image
import gradio as gr

from src.inference import PlantDiseaseService

TITLE = "Smart Crop Health Monitoring"
DISCLAIMER = (
    "This tool is intended for decision support only. "
    "Predictions should be interpreted alongside domain knowledge and, "
    "where necessary, expert agronomic advice."
)

service = None
service_error = None

try:
    service = PlantDiseaseService("artifacts")
except Exception as e:
    service_error = str(e)


def format_status(label: str) -> str:
    return f"### Status\n{label}"


def format_summary(metrics: dict, model_name: str, num_classes: int) -> str:
    lines = [
        f"**Model:** {model_name}",
        f"**Classes:** {num_classes}",
    ]
    if metrics:
        if "test_accuracy" in metrics:
            lines.append(f"**Test Accuracy:** {metrics['test_accuracy'] * 100:.2f}%")
        if "macro_f1" in metrics:
            lines.append(f"**Macro F1:** {metrics['macro_f1']:.3f}")
        if "epochs_completed" in metrics:
            lines.append(f"**Epochs Completed:** {metrics['epochs_completed']}")
    return "\n\n".join(lines)


def coerce_result(result: dict):
    # predicted class
    display_class = result.get("display_class") or result.get("raw_class") or "Unknown"

    # confidence
    if "confidence_pct" in result:
        confidence = result["confidence_pct"]
    elif "confidence" in result:
        try:
            confidence = f"{float(result['confidence']) * 100:.2f}%"
        except Exception:
            confidence = str(result["confidence"])
    else:
        confidence = ""

    # health badge
    health_badge = result.get("health_badge")
    if not health_badge:
        healthy_flag = result.get("healthy_flag", "")
        if healthy_flag:
            if "healthy" in healthy_flag.lower():
                health_badge = f"🟢 {healthy_flag}"
            else:
                health_badge = f"🟠 {healthy_flag}"
        else:
            health_badge = "—"

    # top-5 table
    if "top5_table" in result and isinstance(result["top5_table"], list):
        top5_table = result["top5_table"]
    elif "top5" in result:
        top5 = result["top5"]
        if isinstance(top5, dict):
            top5_table = [[k, f"{float(v) * 100:.2f}%"] for k, v in top5.items()]
        elif isinstance(top5, list):
            top5_table = []
            for item in top5:
                if isinstance(item, (list, tuple)) and len(item) >= 2:
                    name, val = item[0], item[1]
                    try:
                        pct = f"{float(val) * 100:.2f}%"
                    except Exception:
                        pct = str(val)
                    top5_table.append([str(name), pct])
                else:
                    top5_table.append([str(item), ""])
        else:
            top5_table = []
    else:
        top5_table = []

    overlay = result.get("overlay")
    metrics = result.get("metrics", {})
    model_name = result.get("model_name", "EfficientNet-B2 / ResNet-50")
    num_classes = result.get("num_classes", 23)

    summary = format_summary(metrics, model_name, num_classes)

    return display_class, confidence, format_status(health_badge), top5_table, overlay, summary


def predict_from_path(image_path: str):
    if not image_path:
        return (
            "No image uploaded.",
            "",
            "",
            [],
            None,
            "Upload a leaf image to begin.",
            DISCLAIMER,
        )

    if service_error is not None:
        return (
            "Model not ready.",
            "",
            "",
            [],
            None,
            f"Artifact error: {service_error}",
            DISCLAIMER,
        )

    image = Image.open(image_path).convert("RGB")
    result = service.predict_with_explainability(image)

    display_class, confidence, status_md, top5_table, overlay, summary = coerce_result(result)

    return (
        display_class,
        confidence,
        status_md,
        top5_table,
        overlay,
        summary,
        DISCLAIMER,
    )


CUSTOM_CSS = """
.gradio-container {
    max-width: 1200px !important;
}
.hero {
    border: 1px solid #e5e7eb;
    border-radius: 20px;
    padding: 22px;
    margin-bottom: 16px;
    background: linear-gradient(135deg, #f8fafc 0%, #eef6ff 100%);
}
.card {
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 14px;
    background: white;
}
"""

with gr.Blocks(title=TITLE) as demo:
    gr.HTML(f"<style>{CUSTOM_CSS}</style>")

    with gr.Column(elem_classes=["hero"]):
        gr.Markdown(
            f"# {TITLE}\n"
            "### Local VS Code UI for prediction, confidence, top-5 output, and Grad-CAM explainability"
        )

    with gr.Row():
        with gr.Column(scale=5):
            with gr.Group(elem_classes=["card"]):
                image_input = gr.Image(
                    type="filepath",
                    sources=["upload"],
                    label="Upload Leaf Image",
                    height=420
                )
                run_btn = gr.Button("Run Prediction", variant="primary")

        with gr.Column(scale=4):
            with gr.Group(elem_classes=["card"]):
                pred_output = gr.Textbox(label="Predicted Class")
                conf_output = gr.Textbox(label="Confidence")
                status_output = gr.Markdown("### Status\n—")
                summary_output = gr.Markdown("Model summary will appear here.")

    with gr.Row():
        with gr.Column(scale=4):
            top5_output = gr.Dataframe(
                headers=["Class", "Probability"],
                datatype=["str", "str"],
                row_count=5,
                column_count=(2, "fixed"),
                label="Top-5 Predictions"
            )
        with gr.Column(scale=5):
            cam_output = gr.Image(label="Grad-CAM Overlay", height=420)

    with gr.Accordion("Responsible Use", open=True):
        disclaimer_output = gr.Markdown(DISCLAIMER)

    run_btn.click(
        fn=predict_from_path,
        inputs=[image_input],
        outputs=[
            pred_output,
            conf_output,
            status_output,
            top5_output,
            cam_output,
            summary_output,
            disclaimer_output,
        ],
    )

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        inbrowser=True,
        show_error=True
    )