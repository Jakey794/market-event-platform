from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.domain.models.enums import AlertType

PRICE_ALERT_TYPES = {
    AlertType.PRICE_ABOVE,
    AlertType.PRICE_BELOW,
}
PERCENT_ALERT_TYPES = {
    AlertType.PCT_MOVE_UP_1D,
    AlertType.PCT_MOVE_DOWN_1D,
}


class AlertCreateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    asset_id: int = Field(..., gt=0)
    alert_type: AlertType
    threshold_value: Decimal | None = None
    percent_value: Decimal | None = None
    cooldown_minutes: int = Field(default=60, ge=0)
    is_active: bool = True

    @model_validator(mode="after")
    def validate_values(self) -> "AlertCreateRequest":
        if self.alert_type in PRICE_ALERT_TYPES:
            if self.threshold_value is None or self.percent_value is not None:
                raise ValueError(
                    "price alerts require threshold_value and must not include percent_value"
                )

        if self.alert_type in PERCENT_ALERT_TYPES:
            if self.percent_value is None or self.threshold_value is not None:
                raise ValueError(
                    "percent alerts require percent_value and must not include threshold_value"
                )

        return self


class AlertUpdateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    alert_type: AlertType | None = None
    threshold_value: Decimal | None = None
    percent_value: Decimal | None = None
    cooldown_minutes: int | None = Field(default=None, ge=0)
    is_active: bool | None = None

    @model_validator(mode="after")
    def validate_partial_values(self) -> "AlertUpdateRequest":
        if self.threshold_value is not None and self.percent_value is not None:
            raise ValueError("Provide only one of threshold_value or percent_value")

        if self.alert_type in PRICE_ALERT_TYPES and self.percent_value is not None:
            raise ValueError("price alerts must not include percent_value")

        if self.alert_type in PERCENT_ALERT_TYPES and self.threshold_value is not None:
            raise ValueError("percent alerts must not include threshold_value")

        return self


class AlertResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    asset_id: int
    alert_type: AlertType
    threshold_value: Decimal | None
    percent_value: Decimal | None
    cooldown_minutes: int
    is_active: bool
    last_triggered_at: datetime | None
    created_at: datetime
    updated_at: datetime


class AlertListResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    items: list[AlertResponse]