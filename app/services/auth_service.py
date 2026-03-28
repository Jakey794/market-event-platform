from app.core.errors import ServiceNotImplementedError
from app.domain.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.domain.schemas.users import UserPublic


class AuthService:
    def register(self, _payload: RegisterRequest) -> UserPublic:
        raise ServiceNotImplementedError("POST /api/v1/auth/register")

    def login(self, _payload: LoginRequest) -> TokenResponse:
        raise ServiceNotImplementedError("POST /api/v1/auth/login")


def get_auth_service() -> AuthService:
    return AuthService()