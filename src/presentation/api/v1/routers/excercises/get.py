from fastapi import APIRouter
from presentation.api.v1.schemas.excercises import (
    GetExcerciseResponse,
)

router = APIRouter()


@router.get(
    path="/{id}/",
    summary="Получить упражнение",
    description="Возвращает упражнение по идентификатору",
    response_description="Детали упражнения",
    response_model=GetExcerciseResponse,
)
async def get_excercise() -> GetExcerciseResponse:
    pass
