from fastapi import APIRouter
from ..core.config import config

router= APIRouter()

@router.get("/status", tags=["Status"])
async def get_status():
    return {"status": "💚 Nautilus API is online!"}

@router.get("/health", tags=["Status"])
async def get_health():
    return {"health": "🌊 Nautilus API is healthy!"}

@router.get("/info", tags=["General"])
async def get_info():
    return {
        "info": {
            "title": config.PROJECT_NAME,
            "description": config.PROJECT_DESC,
            "version": config.VERSION,
        }
    }
