from fastapi import APIRouter

from application.dto.exercises.create_excercise import CreateExerciseInputDTO
from application.use_cases.exercises.create import CreateExerciseUseCase

from presentation.api.v1.schemas.exercises import (
    CreateExerciseRequest,
    CreateExerciseResponse,
)
from presentation.dependencies.uow import UowDep


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
    uow: UowDep,
) -> CreateExerciseResponse:
    dto = CreateExerciseInputDTO(
        title=data.title,
        short=data.short,
        category_id=data.category_id,
    )
    use_case = CreateExerciseUseCase(uow=uow)
    exercise = await use_case.execute(dto=dto)
