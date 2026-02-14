from fastapi import APIRouter

from presentation.api.v1.schemas.template_exercises import (
    DeleteTemplateExerciseRequest,
    DeleteTemplateExerciseResponse,
)

router = APIRouter()


@router.delete(
    path="/{id}/",
    summary="Удалить упражнение из шаблона",
    description="Удаляет упражнение из шаблона по идентификатору",
    response_description="Результат удаления",
    response_model=DeleteTemplateExerciseResponse,
)
async def delete_template_excercise(
    data: DeleteTemplateExerciseRequest,
) -> DeleteTemplateExerciseResponse:
    pass
