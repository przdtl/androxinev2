from fastapi import APIRouter

from presentation.api.v1.schemas.exercises import (
    RestoreExerciseRequest,
    RestoreExerciseResponse,
)

router = APIRouter()


@router.post(
    path="/{id}/restore/",
    summary="Восстановить упражнение",
    description="Восстанавливает упражнение по идентификатору",
    response_description="Результат восстановления",
    response_model=RestoreExerciseResponse,
)
async def restore_excercise(
    data: RestoreExerciseRequest,
) -> RestoreExerciseResponse:
    pass
