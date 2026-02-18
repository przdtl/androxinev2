import uuid

from fastapi import APIRouter

from dto.exercises.get_excercise import GetExerciseInputDTO
from use_cases.exercises.get import GetExerciseUseCase

from ..schemas.common import CategorySchema
from ..schemas.exercises import (
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
) -> GetExerciseResponse:
    dto = GetExerciseInputDTO(id=id)
    use_case = GetExerciseUseCase()
    exercise = await use_case.execute(input_dto=dto)

    return GetExerciseResponse(
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
