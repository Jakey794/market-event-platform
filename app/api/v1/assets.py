from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query

from app.api.responses import NOT_IMPLEMENTED_RESPONSE
from app.domain.schemas.assets import AssetLatestResponse, AssetSearchResponse
from app.services.assets_service import AssetsService, get_assets_service

router = APIRouter(tags=["assets"])


@router.get(
    "/search",
    response_model=AssetSearchResponse,
    summary="Search assets",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def search_assets(
    q: str = Query(..., min_length=1, max_length=50, description="Search term"),
    limit: int = Query(20, ge=1, le=100, description="Maximum number of results"),
    service: Annotated[AssetsService, Depends(get_assets_service)] = None,
) -> AssetSearchResponse:
    return service.search_assets(query=q, limit=limit)


@router.get(
    "/{symbol}/latest",
    response_model=AssetLatestResponse,
    summary="Get latest price for a symbol",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def get_latest_asset_price(
    symbol: str = Path(..., min_length=1, max_length=32, description="Ticker symbol"),
    service: Annotated[AssetsService, Depends(get_assets_service)] = None,
) -> AssetLatestResponse:
    return service.get_latest_by_symbol(symbol=symbol)