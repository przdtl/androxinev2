from fastapi import APIRouter

from presentation.api.v1.schemas.templates import (
    GetTodayTemplatesResponse,
)

router = APIRouter()


@router.get(
    path="/today/",
    summary="Шаблоны тренировок на сегодня",
    description="Возвращает список шаблонов тренировок на сегодня",
    response_description="Список шаблонов тренировок на сегодня",
    response_model=GetTodayTemplatesResponse,
)
async def get_today_templates() -> GetTodayTemplatesResponse:
    pass
