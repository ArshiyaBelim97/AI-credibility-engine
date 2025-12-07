from fastapi import FastAPI, UploadFile, File
from app.services.text_detector import analyze_text
from app.services.image_detector import analyze_image
from app.services.audio_detector import analyze_audio
from app.services.video_detector import analyze_video

app = FastAPI(title="AI Credibility Engine")

@app.get("/")
def home():
    return {"message": "AI Credibility Engine backend running"}

@app.post("/analyze-text")
async def analyze_text_api(data: dict):
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}

    result = analyze_text(text)
    return result


@app.post("/analyze-image")
def analyze_image_endpoint(img: dict):
    """
    Expects JSON like:
    { "image_base64": "...." }
    """
    base64_img = img.get("image_base64")

    if not base64_img:
        return {"error": "image_base64 missing"}

    result = analyze_image(base64_img)
    return result

@app.post("/analyze/audio")
async def analyze_audio_endpoint(file: UploadFile = File(...)):
    result = await analyze_audio(file)
    return {"result": result}

@app.post("/analyze/video")
async def analyze_video_endpoint(file: UploadFile = File(...)):
    result = await analyze_video(file)
    return {"result": result}
# TEXT DETECTOR ENDPOINT
from app.services.text_detector import analyze_text


