from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from app.domain.models.enums import AssetType


class AssetSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    symbol: str
    name: str
    asset_type: AssetType
    exchange: str
    currency: str
    is_active: bool


class AssetSearchResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    items: list[AssetSummary]


class AssetLatestResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    symbol: str
    price: Decimal
    as_of: datetime
    currency: str
    source: str