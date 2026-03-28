from app.core.config import get_settings
from app.domain.schemas.health import HealthResponse


class HealthService:
    def get_health(self) -> HealthResponse:
        settings = get_settings()
        return HealthResponse(
            status="ok",
            service=settings.app_name,
            environment=settings.app_env,
        )


def get_health_service() -> HealthService:
    return HealthService()