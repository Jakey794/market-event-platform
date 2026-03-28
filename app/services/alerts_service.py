from app.core.errors import ServiceNotImplementedError
from app.domain.schemas.alerts import (
    AlertCreateRequest,
    AlertListResponse,
    AlertResponse,
    AlertUpdateRequest,
)
from app.domain.schemas.common import MessageResponse


class AlertsService:
    def create_alert(self, _payload: AlertCreateRequest) -> AlertResponse:
        raise ServiceNotImplementedError("POST /api/v1/alerts")

    def list_alerts(self) -> AlertListResponse:
        raise ServiceNotImplementedError("GET /api/v1/alerts")

    def update_alert(self, alert_id: int, _payload: AlertUpdateRequest) -> AlertResponse:
        _ = alert_id
        raise ServiceNotImplementedError("PATCH /api/v1/alerts/{alert_id}")

    def delete_alert(self, alert_id: int) -> MessageResponse:
        _ = alert_id
        raise ServiceNotImplementedError("DELETE /api/v1/alerts/{alert_id}")


def get_alerts_service() -> AlertsService:
    return AlertsService()