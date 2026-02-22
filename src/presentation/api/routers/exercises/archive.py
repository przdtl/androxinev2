import uuid

from fastapi import APIRouter

from dto.exercises import ArchiveExerciseInputDTO
from use_cases.exercises import ArchiveExerciseUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.common import CategorySchema
from presentation.api.schemas.exercises import (
    ArchiveExerciseResponse,
)

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
    uow: UOWDep,
    user_id: UserDep,
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
        ),
        created_at=exercise.created_at,
        updated_at=exercise.updated_at,
        is_archived=exercise.is_archived,
    )
