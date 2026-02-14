from fastapi import APIRouter

from presentation.api.v1.schemas.template_exercises import (
    UpdateTemplateExerciseRequest,
    UpdateTemplateExerciseResponse,
)

router = APIRouter()


@router.patch(
    path="/{id}/",
    summary="Обновить упражнение в шаблоне",
    description="Обновляет упражнение в шаблоне по идентификатору",
    response_description="Обновленные детали упражнения в шаблоне",
    response_model=UpdateTemplateExerciseResponse,
)
async def update_template_excercise(
    data: UpdateTemplateExerciseRequest,
) -> UpdateTemplateExerciseResponse:
    pass
