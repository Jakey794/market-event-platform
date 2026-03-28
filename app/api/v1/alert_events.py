from typing import Annotated

from fastapi import APIRouter, Depends, Query

from app.api.responses import NOT_IMPLEMENTED_RESPONSE
from app.domain.schemas.alert_events import AlertEventListResponse
from app.services.alert_events_service import AlertEventsService, get_alert_events_service

router = APIRouter(tags=["alert-events"])


@router.get(
    "",
    response_model=AlertEventListResponse,
    summary="List alert events",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def list_alert_events(
    symbol: str | None = Query(default=None, min_length=1, max_length=32),
    alert_id: int | None = Query(default=None, gt=0),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    service: Annotated[AlertEventsService, Depends(get_alert_events_service)] = None,
) -> AlertEventListResponse:
    return service.list_alert_events(
        symbol=symbol,
        alert_id=alert_id,
        limit=limit,
        offset=offset,
    )