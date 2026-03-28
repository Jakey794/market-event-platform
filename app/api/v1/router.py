from fastapi import APIRouter

from app.api.v1 import alert_events, alerts, assets, auth, health, users, watchlists

router = APIRouter()
router.include_router(health.router)
router.include_router(auth.router, prefix="/auth")
router.include_router(users.router)
router.include_router(assets.router, prefix="/assets")
router.include_router(watchlists.router, prefix="/watchlists")
router.include_router(alerts.router, prefix="/alerts")
router.include_router(alert_events.router, prefix="/alert-events")