import uuid

from fastapi import APIRouter

from dto.templates.delete_template import DeleteTemplateInputDTO
from use_cases.templates.delete import DeleteTemplateUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.templates import (
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
    id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> DeleteTemplateResponse:
    dto = DeleteTemplateInputDTO(id=id)
    use_case = DeleteTemplateUseCase(uow=uow)
    await use_case.execute(input_dto=dto)

    return DeleteTemplateResponse()
