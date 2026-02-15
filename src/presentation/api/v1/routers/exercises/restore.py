import uuid

from fastapi import APIRouter

from application.dto.exercises.restore_excercise import RestoreExerciseInputDTO
from application.use_cases.exercises.restore import RestoreExerciseUseCase

from presentation.api.v1.schemas.common import CategorySchema
from presentation.api.v1.schemas.exercises import (
    RestoreExerciseRequest,
    RestoreExerciseResponse,
)
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.post(
    path="/{id}/restore/",
    summary="Восстановить упражнение",
    description="Восстанавливает упражнение по идентификатору",
    response_description="Результат восстановления",
    response_model=RestoreExerciseResponse,
)
async def restore_excercise(
    id: uuid.UUID,
    data: RestoreExerciseRequest,
    uow: UowDep,
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
            created_at=exercise.category.created_at,
            updated_at=exercise.category.updated_at,
        ),
        created_at=exercise.created_at,
        updated_at=exercise.updated_at,
        is_archived=exercise.is_archived,
    )
