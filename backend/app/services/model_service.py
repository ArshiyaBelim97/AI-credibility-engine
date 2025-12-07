from typing import Any, Dict
from app.models.text_detector import TextDetector
from app.models.image_detector import ImageDetector
# audio/video detectors can be added similarly

# Create a singleton-like service to reuse detectors across requests
class ModelService:
    def __init__(self):
        # instantiate detectors (lightweight default implementations)
        self.text_detector = TextDetector()
        self.image_detector = ImageDetector()

    # text
    def analyze_text(self, text: str) -> Dict[str, Any]:
        text_pred = self.text_detector.predict(text)
        # credibility scoring: simple mapping & normalization
        score = (1 - text_pred["ai_confidence"]) * 100  # higher => more credible (human)
        return {
            "source": "text",
            "label": text_pred["label"],
            "ai_confidence": text_pred["ai_confidence"],
            "human_confidence": text_pred["human_confidence"],
            "credibility_score": round(score, 2)
        }

    # image
    def analyze_image(self, image_bytes: bytes, filename: str = "") -> Dict[str, Any]:
        img_pred = self.image_detector.predict(image_bytes)
        score = (1 - img_pred["ai_confidence"]) * 100
        return {
            "source": "image",
            "filename": filename,
            "label": img_pred["label"],
            "ai_confidence": img_pred["ai_confidence"],
            "human_confidence": img_pred["human_confidence"],
            "credibility_score": round(score, 2)
        }

    # audio (stub)
    def analyze_audio(self, audio_bytes: bytes, filename: str = "") -> Dict[str, Any]:
        # stub: return unknown
        return {"source": "audio", "filename": filename, "label": "unknown", "ai_confidence": 0.5, "credibility_score": 50.0}

    # video (stub)
    def analyze_video(self, video_bytes: bytes, filename: str = "") -> Dict[str, Any]:
        return {"source": "video", "filename": filename, "label": "unknown", "ai_confidence": 0.5, "credibility_score": 50.0}

# dependency helpers for FastAPI
_model_service = None
def get_model_service():
    global _model_service
    if _model_service is None:
        _model_service = ModelService()
    return _model_service
