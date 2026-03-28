from app.core.errors import ServiceNotImplementedError
from app.domain.schemas.assets import AssetLatestResponse, AssetSearchResponse


class AssetsService:
    def search_assets(self, query: str, limit: int) -> AssetSearchResponse:
        _ = (query, limit)
        raise ServiceNotImplementedError("GET /api/v1/assets/search")

    def get_latest_by_symbol(self, symbol: str) -> AssetLatestResponse:
        _ = symbol
        raise ServiceNotImplementedError("GET /api/v1/assets/{symbol}/latest")


def get_assets_service() -> AssetsService:
    return AssetsService()