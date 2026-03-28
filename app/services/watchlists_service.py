from app.core.errors import ServiceNotImplementedError
from app.domain.schemas.common import MessageResponse
from app.domain.schemas.watchlists import (
    WatchlistCreateRequest,
    WatchlistItemCreateRequest,
    WatchlistItemResponse,
    WatchlistListResponse,
    WatchlistResponse,
)


class WatchlistsService:
    def create_watchlist(self, _payload: WatchlistCreateRequest) -> WatchlistResponse:
        raise ServiceNotImplementedError("POST /api/v1/watchlists")

    def list_watchlists(self) -> WatchlistListResponse:
        raise ServiceNotImplementedError("GET /api/v1/watchlists")

    def add_item(
        self,
        watchlist_id: int,
        _payload: WatchlistItemCreateRequest,
    ) -> WatchlistItemResponse:
        _ = watchlist_id
        raise ServiceNotImplementedError("POST /api/v1/watchlists/{watchlist_id}/items")

    def remove_item(self, watchlist_id: int, asset_id: int) -> MessageResponse:
        _ = (watchlist_id, asset_id)
        raise ServiceNotImplementedError(
            "DELETE /api/v1/watchlists/{watchlist_id}/items/{asset_id}"
        )


def get_watchlists_service() -> WatchlistsService:
    return WatchlistsService()