from fastapi import APIRouter
from presentation.api.v1.schemas.template_excercises import (
    ListTemplateExcercisesResponse,
)

router = APIRouter()


@router.get(
    path="/",
    summary="Список упражнений в шаблоне",
    description="Возвращает список упражнений в шаблоне",
    response_description="Список упражнений в шаблоне",
    response_model=ListTemplateExcercisesResponse,
)
async def list_template_excercises() -> ListTemplateExcercisesResponse:
    pass
