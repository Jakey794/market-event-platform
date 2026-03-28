from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.responses import NOT_IMPLEMENTED_RESPONSE
from app.domain.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.domain.schemas.users import UserPublic
from app.services.auth_service import AuthService, get_auth_service

router = APIRouter(tags=["auth"])


@router.post(
    "/register",
    response_model=UserPublic,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def register_user(
    payload: RegisterRequest,
    service: Annotated[AuthService, Depends(get_auth_service)],
) -> UserPublic:
    return service.register(payload)


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Login",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def login_user(
    payload: LoginRequest,
    service: Annotated[AuthService, Depends(get_auth_service)],
) -> TokenResponse:
    return service.login(payload)