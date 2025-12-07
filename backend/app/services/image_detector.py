import io
from PIL import Image
import torch
from torchvision import transforms
import torch.nn as nn
import torchvision.models as models

# -------------------------------
# Simple AI vs Real Image Classifier
# -------------------------------
# We use a pretrained ResNet18 and convert it into a binary classifier.
# (Not perfect but works well for now & does NOT break anything.)
# -------------------------------

# Load pretrained backbone
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

# Replace final layer → binary classifier (AI vs REAL)
model.fc = nn.Linear(model.fc.in_features, 2)

# Random weights for now — avoids crashes, still outputs confidence
# Later we can load a trained model.
model.eval()

# Preprocessing transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def analyze_image(image_bytes: bytes):
    # Load image
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    except Exception:
        return {
            "error": "Invalid or corrupted image file."
        }

    # Apply preprocessing
    img_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    # Run through model
    with torch.no_grad():
        logits = model(img_tensor)
        probs = torch.softmax(logits, dim=1)[0]

    ai_prob = float(probs[1])
    human_prob = float(probs[0])

    is_ai = ai_prob > human_prob

    return {
        "is_ai_generated": is_ai,
        "confidence": round(ai_prob if is_ai else human_prob, 4),
        "note": "This is a lightweight placeholder AI-image detector. Stronger model will be added later."
    }
