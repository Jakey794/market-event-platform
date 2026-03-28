from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.responses import NOT_IMPLEMENTED_RESPONSE
from app.domain.schemas.users import CurrentUserResponse
from app.services.users_service import UsersService, get_users_service

router = APIRouter(tags=["users"])


@router.get(
    "/me",
    response_model=CurrentUserResponse,
    summary="Get current user",
    responses=NOT_IMPLEMENTED_RESPONSE,
)
def get_current_user(
    service: Annotated[UsersService, Depends(get_users_service)],
) -> CurrentUserResponse:
    return service.get_current_user()