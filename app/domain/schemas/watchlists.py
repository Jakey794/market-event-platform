from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class WatchlistCreateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., min_length=1, max_length=100)


class WatchlistResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    created_at: datetime


class WatchlistListResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    items: list[WatchlistResponse]


class WatchlistItemCreateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    asset_id: int = Field(..., gt=0)


class WatchlistItemResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    watchlist_id: int
    asset_id: int
    created_at: datetime