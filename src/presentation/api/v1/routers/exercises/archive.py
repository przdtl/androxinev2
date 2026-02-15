import uuid

from fastapi import APIRouter

from application.dto.exercises.archive_excercise import ArchiveExerciseInputDTO
from application.use_cases.exercises.archive import ArchiveExerciseUseCase

from presentation.api.v1.schemas.common import CategorySchema
from presentation.api.v1.schemas.exercises import (
    ArchiveExerciseRequest,
    ArchiveExerciseResponse,
)
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.post(
    path="/{id}/archive/",
    deprecated=True,
    summary="Архивировать упражнение",
    description="Архивирует упражнение по идентификатору",
    response_description="Результат архивирования",
    response_model=ArchiveExerciseResponse,
)
async def archive_excercise(
    id: uuid.UUID,
    data: ArchiveExerciseRequest,
    uow: UowDep,
) -> ArchiveExerciseResponse:
    dto = ArchiveExerciseInputDTO(id=id)
    use_case = ArchiveExerciseUseCase(uow=uow)
    exercise = await use_case.execute(input_dto=dto)

    return ArchiveExerciseResponse(
        id=exercise.id,
        title=exercise.title,
        short=exercise.short,
        category=CategorySchema(
            id=exercise.category.id,
            title=exercise.category.title,
            created_at=exercise.category.created_at,
            updated_at=exercise.category.updated_at,
        ),
        created_at=exercise.created_at,
        updated_at=exercise.updated_at,
        is_archived=exercise.is_archived,
    )
