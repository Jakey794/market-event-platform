from fastapi import APIRouter

from app.api.legacy import router as legacy_router
from app.api.v1.router import router as v1_router

router = APIRouter()
router.include_router(legacy_router)
router.include_router(v1_router, prefix="/api/v1")