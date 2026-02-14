from fastapi import APIRouter
from presentation.api.v1.schemas.excercises import (
    RestoreExcerciseRequest,
    RestoreExcerciseResponse,
)

router = APIRouter()


@router.post(
    path="/{id}/restore/",
    summary="Восстановить упражнение",
    description="Восстанавливает упражнение по идентификатору",
    response_description="Результат восстановления",
    response_model=RestoreExcerciseResponse,
)
async def restore_excercise(
    data: RestoreExcerciseRequest,
) -> RestoreExcerciseResponse:
    pass
