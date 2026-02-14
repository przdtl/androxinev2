from fastapi import APIRouter
from presentation.api.v1.schemas.excercises import (
    ListUserExcercisesResponse,
)

router = APIRouter()


@router.get(
    path="/user/",
    summary="Список упражнений пользователя",
    description="Возвращает список упражнений пользователя",
    response_description="Список упражнений пользователя",
    response_model=ListUserExcercisesResponse,
)
async def list_user_excercises() -> ListUserExcercisesResponse:
    pass
