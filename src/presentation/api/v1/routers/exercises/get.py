from fastapi import APIRouter

from presentation.api.v1.schemas.exercises import (
    GetExerciseResponse,
)

router = APIRouter()


@router.get(
    path="/{id}/",
    summary="Получить упражнение",
    description="Возвращает упражнение по идентификатору",
    response_description="Детали упражнения",
    response_model=GetExerciseResponse,
)
async def get_excercise() -> GetExerciseResponse:
    pass
