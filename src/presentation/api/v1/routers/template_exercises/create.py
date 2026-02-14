from fastapi import APIRouter

from presentation.api.v1.schemas.template_exercises import (
    CreateTemplateExerciseRequest,
    CreateTemplateExerciseResponse,
)

router = APIRouter()


@router.post(
    path="/",
    summary="Добавить упражнение в шаблон",
    description="Добавляет упражнение в шаблон тренировок",
    response_description="Детали упражнения в шаблоне",
    response_model=CreateTemplateExerciseResponse,
)
async def create_template_exercise(
    data: CreateTemplateExerciseRequest,
) -> CreateTemplateExerciseResponse:
    pass
