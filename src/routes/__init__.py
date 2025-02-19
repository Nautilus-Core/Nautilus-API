from fastapi import APIRouter
from .data import router as data_router
from .general import router as general_router

router = APIRouter()

router.include_router(data_router, prefix="/data", tags=["Data"])
router.include_router(general_router, prefix="", tags=["General"])