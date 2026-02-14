from fastapi import APIRouter
from presentation.api.v1.schemas.template_excercises import (
    CreateTemplateExcerciseRequest,
    CreateTemplateExcerciseResponse,
)

router = APIRouter()


@router.post(
    path="/",
    summary="Добавить упражнение в шаблон",
    description="Добавляет упражнение в шаблон тренировок",
    response_description="Детали упражнения в шаблоне",
    response_model=CreateTemplateExcerciseResponse,
)
async def create_template_excercise(
    data: CreateTemplateExcerciseRequest,
) -> CreateTemplateExcerciseResponse:
    pass
