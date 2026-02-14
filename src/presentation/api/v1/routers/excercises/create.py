from fastapi import APIRouter
from presentation.api.v1.schemas.excercises import (
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
async def create_excercise(
    data: CreateExerciseRequest,
) -> CreateExerciseResponse:
    pass
