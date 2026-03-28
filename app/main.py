from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.api.router import router as api_router
from app.core.config import get_settings
from app.core.errors import ServiceNotImplementedError
from app.domain.schemas.common import ErrorResponse

TAGS_METADATA = [
    {"name": "health", "description": "Health checks for the service."},
    {"name": "auth", "description": "Registration and login endpoints."},
    {"name": "users", "description": "Current-user endpoints."},
    {"name": "assets", "description": "Asset lookup and latest-price endpoints."},
    {
        "name": "watchlists",
        "description": "Watchlist creation and watchlist membership management.",
    },
    {"name": "alerts", "description": "Alert creation and lifecycle management."},
    {"name": "alert-events", "description": "Triggered alert history."},
]


def create_app() -> FastAPI:
    settings = get_settings()

    application = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="Backend-first Market Watch & Alerts API. Step 6 API shell.",
        debug=settings.debug,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_tags=TAGS_METADATA,
    )
    application.include_router(api_router)

    @application.exception_handler(ServiceNotImplementedError)
    async def handle_service_not_implemented(
        request: Request,
        exc: ServiceNotImplementedError,
    ) -> JSONResponse:
        error = ErrorResponse(
            error="not_implemented",
            message=str(exc),
        )
        return JSONResponse(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            content=error.model_dump(),
        )

    return application


app = create_app()