from fastapi import APIRouter
from presentation.api.v1.schemas.excercises import (
    ArchiveExcerciseRequest,
    ArchiveExcerciseResponse,
)

router = APIRouter()


@router.post(
    path="/{id}/archive/",
    summary="Архивировать упражнение",
    description="Архивирует упражнение по идентификатору",
    response_description="Результат архивирования",
    response_model=ArchiveExcerciseResponse,
)
async def archive_excercise(
    data: ArchiveExcerciseRequest,
) -> ArchiveExcerciseResponse:
    pass
