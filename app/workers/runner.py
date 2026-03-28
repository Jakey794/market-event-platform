import logging
import time

from app.core.config import get_settings
from app.core.database import ping_database

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    settings = get_settings()

    logger.info(
        "worker starting app_name=%s app_env=%s heartbeat_seconds=%s",
        settings.app_name,
        settings.app_env,
        settings.worker_heartbeat_seconds,
    )

    db_ok = ping_database()
    logger.info("worker database connectivity check ok=%s", db_ok)

    while True:
        logger.info(
            "worker heartbeat - placeholder process alive; scheduling logic will be added later"
        )
        time.sleep(settings.worker_heartbeat_seconds)


if __name__ == "__main__":
    main()