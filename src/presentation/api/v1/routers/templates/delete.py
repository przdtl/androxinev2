import uuid

from fastapi import APIRouter

from application.dto.templates.delete_template import DeleteTemplateInputDTO
from application.use_cases.templates.delete import DeleteTemplateUseCase

from presentation.api.v1.schemas.templates import (
    DeleteTemplateRequest,
    DeleteTemplateResponse,
)
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.delete(
    path="/{id}/",
    summary="Удалить шаблон тренировки",
    description="Удаляет шаблон тренировки по идентификатору",
    response_description="Результат удаления",
    response_model=DeleteTemplateResponse,
)
async def delete_template(
    id: uuid.UUID,
    data: DeleteTemplateRequest,
    uow: UowDep,
) -> DeleteTemplateResponse:
    dto = DeleteTemplateInputDTO(id=id)
    use_case = DeleteTemplateUseCase(uow=uow)
    await use_case.execute(input_dto=dto)

    return DeleteTemplateResponse()
