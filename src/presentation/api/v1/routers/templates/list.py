from fastapi import APIRouter
from presentation.api.v1.schemas.templates import (
    ListTemplatesResponse,
)

router = APIRouter()


@router.get(
    path="/",
    summary="Список шаблонов тренировок",
    description="Возвращает список шаблонов тренировок",
    response_description="Список шаблонов тренировок",
    response_model=ListTemplatesResponse,
)
async def list_templates() -> ListTemplatesResponse:
    pass
