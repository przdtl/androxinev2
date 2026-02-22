import uuid

from fastapi import APIRouter

from dto.exercises import GetExerciseInputDTO
from use_cases.exercises import GetExerciseUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.common import CategorySchema
from presentation.api.schemas.exercises import (
    GetExerciseResponse,
)

router = APIRouter()


@router.get(
    path="/{id}/",
    summary="Получить упражнение",
    description="Возвращает упражнение по идентификатору",
    response_description="Детали упражнения",
    response_model=GetExerciseResponse,
)
async def get_excercise(
    id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> GetExerciseResponse:
    dto = GetExerciseInputDTO(
        exercise_id=id,
        user_id=user_id,
    )
    use_case = GetExerciseUseCase(uow=uow)
    exercise = await use_case.execute(input_dto=dto)

    return GetExerciseResponse(
        id=exercise.id,
        title=exercise.title,
        short=exercise.short,
        category=CategorySchema(
            id=exercise.category.id,
            title=exercise.category.title,
        ),
        is_archived=exercise.is_archived,
    )
