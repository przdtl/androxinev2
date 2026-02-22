import uuid

from fastapi import APIRouter

from dto.exercises import UpdateExerciseInputDTO
from use_cases.exercises import UpdateExerciseUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.common import CategorySchema
from presentation.api.schemas.exercises import (
    UpdateExerciseRequest,
    UpdateExerciseResponse,
)

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
    uow: UOWDep,
    user_id: UserDep,
) -> UpdateExerciseResponse:
    dto = UpdateExerciseInputDTO(
        exercise_id=id,
        user_id=user_id,
        title=data.title,
        short=data.short,
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
        ),
        is_archived=exercise.is_archived,
    )
