from typing import Annotated

from fastapi import APIRouter, Depends, Path, status

from app.api.responses import NOT_IMPLEMENTED_RESPONSE
from app.domain.schemas.alerts import (
    AlertCreateRequest,
    AlertListResponse,
    AlertResponse,
    AlertUpdateRequest,
)
from app.domain.schemas.common import MessageResponse
from app.services.alerts_service import AlertsService, get_alerts_service

router = APIRouter(tags=["alerts"])


@router.post(
    "",
    response_model=AlertResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create an alert",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def create_alert(
    payload: AlertCreateRequest,
    service: Annotated[AlertsService, Depends(get_alerts_service)],
) -> AlertResponse:
    return service.create_alert(payload)


@router.get(
    "",
    response_model=AlertListResponse,
    summary="List alerts",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def list_alerts(
    service: Annotated[AlertsService, Depends(get_alerts_service)],
) -> AlertListResponse:
    return service.list_alerts()


@router.patch(
    "/{alert_id}",
    response_model=AlertResponse,
    summary="Update an alert",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def update_alert(
    alert_id: int = Path(..., gt=0),
    payload: AlertUpdateRequest = None,
    service: Annotated[AlertsService, Depends(get_alerts_service)] = None,
) -> AlertResponse:
    return service.update_alert(alert_id=alert_id, payload=payload)


@router.delete(
    "/{alert_id}",
    response_model=MessageResponse,
    summary="Delete an alert",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def delete_alert(
    alert_id: int = Path(..., gt=0),
    service: Annotated[AlertsService, Depends(get_alerts_service)] = None,
) -> MessageResponse:
    return service.delete_alert(alert_id=alert_id)