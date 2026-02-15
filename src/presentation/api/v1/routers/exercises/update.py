import uuid

from fastapi import APIRouter

from application.dto.exercises.update_excercise import UpdateExerciseInputDTO
from application.use_cases.exercises.update import UpdateExerciseUseCase

from presentation.api.v1.schemas.common import CategorySchema
from presentation.api.v1.schemas.exercises import (
    UpdateExerciseRequest,
    UpdateExerciseResponse,
)
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.patch(
    path="/{id}/",
    summary="Обновить упражнение",
    description="Обновляет упражнение по идентификатору",
    response_description="Обновленные детали упражнения",
    response_model=UpdateExerciseResponse,
)
async def update_excercise(
    id: uuid.UUID,
    data: UpdateExerciseRequest,
    uow: UowDep,
) -> UpdateExerciseResponse:
    dto = UpdateExerciseInputDTO(
        id=id,
        title=data.title,
        short=data.short,
        is_archived=data.is_archived,
    )
    use_case = UpdateExerciseUseCase(uow=uow)
    exercise = await use_case.execute(input_dto=dto)

    return UpdateExerciseResponse(
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
