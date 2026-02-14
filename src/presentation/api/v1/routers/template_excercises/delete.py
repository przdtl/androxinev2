from fastapi import APIRouter
from presentation.api.v1.schemas.template_excercises import (
    DeleteTemplateExcerciseRequest,
    DeleteTemplateExcerciseResponse,
)

router = APIRouter()


@router.delete(
    path="/{id}/",
    summary="Удалить упражнение из шаблона",
    description="Удаляет упражнение из шаблона по идентификатору",
    response_description="Результат удаления",
    response_model=DeleteTemplateExcerciseResponse,
)
async def delete_template_excercise(
    data: DeleteTemplateExcerciseRequest,
) -> DeleteTemplateExcerciseResponse:
    pass
