import uuid

from fastapi import APIRouter

from dto.exercises.restore_excercise import RestoreExerciseInputDTO
from use_cases.exercises.restore import RestoreExerciseUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.common import CategorySchema
from presentation.api.schemas.exercises import (
    RestoreExerciseResponse,
)

router = APIRouter()


@router.post(
    path="/{id}/restore/",
    deprecated=True,
    summary="Восстановить упражнение",
    description="Восстанавливает упражнение по идентификатору",
    response_description="Результат восстановления",
    response_model=RestoreExerciseResponse,
)
async def restore_excercise(
    id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> RestoreExerciseResponse:
    dto = RestoreExerciseInputDTO(id=id)
    use_case = RestoreExerciseUseCase(uow=uow)
    exercise = await use_case.execute(input_dto=dto)

    return RestoreExerciseResponse(
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
