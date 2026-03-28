from typing import Annotated

from fastapi import APIRouter, Depends, Path, status

from app.api.responses import NOT_IMPLEMENTED_RESPONSE
from app.domain.schemas.common import MessageResponse
from app.domain.schemas.watchlists import (
    WatchlistCreateRequest,
    WatchlistItemCreateRequest,
    WatchlistItemResponse,
    WatchlistListResponse,
    WatchlistResponse,
)
from app.services.watchlists_service import WatchlistsService, get_watchlists_service

router = APIRouter(tags=["watchlists"])


@router.post(
    "",
    response_model=WatchlistResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a watchlist",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def create_watchlist(
    payload: WatchlistCreateRequest,
    service: Annotated[WatchlistsService, Depends(get_watchlists_service)],
) -> WatchlistResponse:
    return service.create_watchlist(payload)


@router.get(
    "",
    response_model=WatchlistListResponse,
    summary="List watchlists",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def list_watchlists(
    service: Annotated[WatchlistsService, Depends(get_watchlists_service)],
) -> WatchlistListResponse:
    return service.list_watchlists()


@router.post(
    "/{watchlist_id}/items",
    response_model=WatchlistItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add an asset to a watchlist",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def add_watchlist_item(
    watchlist_id: int = Path(..., gt=0),
    payload: WatchlistItemCreateRequest = None,
    service: Annotated[WatchlistsService, Depends(get_watchlists_service)] = None,
) -> WatchlistItemResponse:
    return service.add_item(watchlist_id=watchlist_id, payload=payload)


@router.delete(
    "/{watchlist_id}/items/{asset_id}",
    response_model=MessageResponse,
    summary="Remove an asset from a watchlist",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def remove_watchlist_item(
    watchlist_id: int = Path(..., gt=0),
    asset_id: int = Path(..., gt=0),
    service: Annotated[WatchlistsService, Depends(get_watchlists_service)] = None,
) -> MessageResponse:
    return service.remove_item(watchlist_id=watchlist_id, asset_id=asset_id)