from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from presentation.api.v1.schemas.templates import (
    ListTemplatesResponse,
)

router = APIRouter()


@router.get(
    path="/",
    summary="Список шаблонов тренировок",
    description="Возвращает список шаблонов тренировок",
    response_description="Список шаблонов тренировок",
    response_model=Page[ListTemplatesResponse],
)
async def list_templates(
    params: Params = Depends(),
) -> Page[ListTemplatesResponse]:
    pass
