from fastapi import APIRouter
from presentation.api.v1.schemas.excercises import (
    ListExcercisesResponse,
)

router = APIRouter()


@router.get(
    path="/",
    summary="Список упражнений",
    description="Возвращает список упражнений",
    response_description="Список упражнений",
    response_model=ListExcercisesResponse,
)
async def list_excercises() -> ListExcercisesResponse:
    pass
