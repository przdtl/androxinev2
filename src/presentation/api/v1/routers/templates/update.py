from fastapi import APIRouter
from presentation.api.v1.schemas.templates import (
    UpdateTemplateRequest,
    UpdateTemplateResponse,
)

router = APIRouter()


@router.patch(
    path="/{id}/",
    summary="Обновить шаблон тренировки",
    description="Обновляет шаблон тренировки по идентификатору",
    response_description="Обновленные детали шаблона",
    response_model=UpdateTemplateResponse,
)
async def update_template(
    data: UpdateTemplateRequest,
) -> UpdateTemplateResponse:
    pass
