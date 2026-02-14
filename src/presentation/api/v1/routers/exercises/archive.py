from fastapi import APIRouter

from presentation.api.v1.schemas.exercises import (
    ArchiveExerciseRequest,
    ArchiveExerciseResponse,
)

router = APIRouter()


@router.post(
    path="/{id}/archive/",
    summary="Архивировать упражнение",
    description="Архивирует упражнение по идентификатору",
    response_description="Результат архивирования",
    response_model=ArchiveExerciseResponse,
)
async def archive_excercise(
    data: ArchiveExerciseRequest,
) -> ArchiveExerciseResponse:
    pass
