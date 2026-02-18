from fastapi import APIRouter

from dto.exercises.create_excercise import CreateExerciseInputDTO
from use_cases.exercises.create import CreateExerciseUseCase

from ..schemas.common import CategorySchema
from ..schemas.exercises import (
    CreateExerciseRequest,
    CreateExerciseResponse,
)


router = APIRouter()


@router.post(
    path="/",
    summary="Создать упражнение",
    description="Создает новое упражнение",
    response_description="Детали созданного упражнения",
    response_model=CreateExerciseResponse,
)
async def create_exercise(
    data: CreateExerciseRequest,
) -> CreateExerciseResponse:
    dto = CreateExerciseInputDTO(
        title=data.title,
        short=data.short,
        category_id=data.category_id,
    )
    use_case = CreateExerciseUseCase()
    exercise = await use_case.execute(input_dto=dto)

    return CreateExerciseResponse(
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
