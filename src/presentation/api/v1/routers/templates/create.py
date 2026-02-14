from fastapi import APIRouter
from presentation.api.v1.schemas.templates import (
    CreateTemplateRequest,
    CreateTemplateResponse,
)

router = APIRouter()


@router.post(
    path="/",
    summary="Создать шаблон тренировки",
    description="Создает новый шаблон тренировки",
    response_description="Детали созданного шаблона",
    response_model=CreateTemplateResponse,
)
async def create_template(
    data: CreateTemplateRequest,
) -> CreateTemplateResponse:
    pass
