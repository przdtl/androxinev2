from fastapi import APIRouter

from dto.exercises import CreateExerciseInputDTO
from use_cases.exercises import CreateExerciseUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.common import CategorySchema
from presentation.api.schemas.exercises import (
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
    uow: UOWDep,
    user_id: UserDep,
) -> CreateExerciseResponse:
    dto = CreateExerciseInputDTO(
        user_id=user_id,
        title=data.title,
        short=data.short,
        category_id=data.category_id,
    )
    use_case = CreateExerciseUseCase(uow=uow)
    exercise = await use_case.execute(input_dto=dto)

    return CreateExerciseResponse(
        id=exercise.id,
        title=exercise.title,
        short=exercise.short,
        category=CategorySchema(
            id=exercise.category.id,
            title=exercise.category.title,
        ),
        is_archived=exercise.is_archived,
    )
