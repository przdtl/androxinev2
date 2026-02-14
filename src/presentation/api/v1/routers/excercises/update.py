from fastapi import APIRouter
from presentation.api.v1.schemas.excercises import (
    UpdateExcerciseRequest,
    UpdateExcerciseResponse,
)

router = APIRouter()


@router.patch(
    path="/{id}/",
    summary="Обновить упражнение",
    description="Обновляет упражнение по идентификатору",
    response_description="Обновленные детали упражнения",
    response_model=UpdateExcerciseResponse,
)
async def update_excercise(
    data: UpdateExcerciseRequest,
) -> UpdateExcerciseResponse:
    pass
