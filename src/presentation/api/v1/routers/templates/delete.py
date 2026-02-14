from fastapi import APIRouter
from presentation.api.v1.schemas.templates import (
    DeleteTemplateRequest,
    DeleteTemplateResponse,
)

router = APIRouter()


@router.delete(
    path="/{id}/",
    summary="Удалить шаблон тренировки",
    description="Удаляет шаблон тренировки по идентификатору",
    response_description="Результат удаления",
    response_model=DeleteTemplateResponse,
)
async def delete_template(
    data: DeleteTemplateRequest,
) -> DeleteTemplateResponse:
    pass
