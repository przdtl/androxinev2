from fastapi import APIRouter
from presentation.api.v1.schemas.excercises import (
    UpdateExerciseRequest,
    UpdateExerciseResponse,
)

router = APIRouter()


@router.patch(
    path="/{id}/",
    summary="Обновить упражнение",
    description="Обновляет упражнение по идентификатору",
    response_description="Обновленные детали упражнения",
    response_model=UpdateExerciseResponse,
)
async def update_excercise(
    data: UpdateExerciseRequest,
) -> UpdateExerciseResponse:
    pass
