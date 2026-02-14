from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from presentation.api.v1.schemas.excercises import (
    ListExercisesResponse,
)

router = APIRouter()


@router.get(
    path="/",
    summary="Список упражнений",
    description="Возвращает список упражнений",
    response_description="Список упражнений",
    response_model=Page[ListExercisesResponse],
)
async def list_excercises(
    params: Params = Depends(),
) -> Page[ListExercisesResponse]:
    pass
