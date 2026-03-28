from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class AlertEventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    alert_id: int | None
    asset_id: int
    user_id: int
    triggered_at: datetime
    observed_price: Decimal
    message: str
    event_payload_json: dict[str, object]


class AlertEventListResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    items: list[AlertEventResponse]