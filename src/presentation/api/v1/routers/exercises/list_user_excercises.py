from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from presentation.api.v1.schemas.exercises import (
    ListUserExercisesResponse,
)

router = APIRouter()


@router.get(
    path="/user/",
    summary="Список упражнений пользователя",
    description="Возвращает список упражнений пользователя",
    response_description="Список упражнений пользователя",
    response_model=Page[ListUserExercisesResponse],
)
async def list_user_excercises(
    params: Params = Depends(),
) -> Page[ListUserExercisesResponse]:
    pass
