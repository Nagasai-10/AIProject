from __future__ import annotations


def humanize_label(label: str) -> str:
    text = label.replace("___", " - ").replace("__", " - ").replace("_", " ")
    text = " ".join(text.split())
    return text


def healthy_status(label: str) -> str:
    lower = label.lower()
    return "Healthy" if "healthy" in lower else "Diseased"
