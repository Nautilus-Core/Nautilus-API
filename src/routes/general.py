from fastapi import APIRouter
from ..core.config import config

router= APIRouter()

# Route to get the status of the API
@router.get("/status", tags=["Status"])
async def get_status():
    return {"status": "💚 Nautilus API is online!"}

# Route to get the health of the API
@router.get("/health", tags=["Status"])
async def get_health():
    return {"health": "🌊 Nautilus API is healthy!"}

# Route to get the info of the API
@router.get("/info", tags=["General"])
async def get_info():
    return {
        "info": {
            "title": config.PROJECT_NAME,
            "description": config.PROJECT_DESC,
            "version": config.VERSION,
        }
    }
