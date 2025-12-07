from fastapi import APIRouter, UploadFile, File, Form, Depends
from fastapi.responses import JSONResponse
from typing import Dict, Any
from app.services.model_service import get_model_service

router = APIRouter(prefix="/analyze", tags=["analyze"])

@router.post("/text")
async def analyze_text(text: str = Form(...), svc = Depends(get_model_service)) -> Dict[str, Any]:
    """Analyze a text string and return credibility scores."""
    result = svc.analyze_text(text)
    return JSONResponse(result)

@router.post("/image")
async def analyze_image(file: UploadFile = File(...), svc = Depends(get_model_service)) -> Dict[str, Any]:
    """Analyze an uploaded image (bytes)"""
    image_bytes = await file.read()
    result = svc.analyze_image(image_bytes, filename=file.filename)
    return JSONResponse(result)

@router.post("/audio")
async def analyze_audio(file: UploadFile = File(...), svc = Depends(get_model_service)) -> Dict[str, Any]:
    """Analyze an uploaded audio file (stub)"""
    audio_bytes = await file.read()
    result = svc.analyze_audio(audio_bytes, filename=file.filename)
    return JSONResponse(result)

@router.post("/video")
async def analyze_video(file: UploadFile = File(...), svc = Depends(get_model_service)) -> Dict[str, Any]:
    """Analyze an uploaded video file (stub)"""
    video_bytes = await file.read()
    result = svc.analyze_video(video_bytes, filename=file.filename)
    return JSONResponse(result)
