from app.core.errors import ServiceNotImplementedError
from app.domain.schemas.users import CurrentUserResponse


class UsersService:
    def get_current_user(self) -> CurrentUserResponse:
        raise ServiceNotImplementedError("GET /api/v1/me")


def get_users_service() -> UsersService:
    return UsersService()