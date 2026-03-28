from app.core.errors import ServiceNotImplementedError
from app.domain.schemas.alert_events import AlertEventListResponse


class AlertEventsService:
    def list_alert_events(
        self,
        symbol: str | None,
        alert_id: int | None,
        limit: int,
        offset: int,
    ) -> AlertEventListResponse:
        _ = (symbol, alert_id, limit, offset)
        raise ServiceNotImplementedError("GET /api/v1/alert-events")


def get_alert_events_service() -> AlertEventsService:
    return AlertEventsService()