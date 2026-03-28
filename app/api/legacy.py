from typing import Annotated

from fastapi import APIRouter, Depends

from app.domain.schemas.health import HealthResponse
from app.services.health_service import HealthService, get_health_service

router = APIRouter()


@router.get("/health", include_in_schema=False)
def legacy_health_check(
    service: Annotated[HealthService, Depends(get_health_service)],
) -> HealthResponse:
    return service.get_health()