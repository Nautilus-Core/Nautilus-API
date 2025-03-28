from fastapi import APIRouter
from .general import router as general_router
from .ocean import router as ocean_router
from .weather import router as weather_router

router = APIRouter()

# Include all the routers below
router.include_router(general_router, prefix="", tags=["General"])
router.include_router(ocean_router, prefix="/ocean", tags=["Ocean"])
router.include_router(weather_router, prefix="/weather", tags=["Weather"])