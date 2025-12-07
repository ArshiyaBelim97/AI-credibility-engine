# backend/app/services/text_detector.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load AI detection model (small + fast + works on CPU)
MODEL_NAME = "roberta-base-openai-detector"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)


def analyze_text(text: str) -> dict:
    """
    Returns AI probability and human probability.
    """

    inputs = tokenizer(text, return_tensors="pt", truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probs = torch.softmax(logits, dim=1)

    ai_prob = float(probs[0][1])      # Model index 1 = AI generated
    human_prob = float(probs[0][0])   # Model index 0 = Human

    return {
        "ai_probability": round(ai_prob, 4),
        "human_probability": round(human_prob, 4),
        "classification": "AI-Generated" if ai_prob > 0.5 else "Human"
    }
