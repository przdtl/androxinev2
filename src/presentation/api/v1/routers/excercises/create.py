from fastapi import APIRouter
from presentation.api.v1.schemas.excercises import (
    CreateExcerciseRequest,
    CreateExcerciseResponse,
)

router = APIRouter()


@router.post(
    path="/",
    summary="Создать упражнение",
    description="Создает новое упражнение",
    response_description="Детали созданного упражнения",
    response_model=CreateExcerciseResponse,
)
async def create_excercise(
    data: CreateExcerciseRequest,
) -> CreateExcerciseResponse:
    pass
