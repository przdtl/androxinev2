import uuid

from fastapi import APIRouter, status

from dto.templates.delete_template import DeleteTemplateInputDTO
from use_cases.templates.delete import DeleteTemplateUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep

router = APIRouter()


@router.delete(
    path="/{template_id}/",
    summary="Удалить шаблон тренировки",
    description="Удаляет шаблон тренировки по идентификатору",
    response_description="Результат удаления",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_template(
    template_id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> None:
    dto = DeleteTemplateInputDTO(user_id=user_id, id=template_id)
    use_case = DeleteTemplateUseCase(uow=uow)
    await use_case.execute(input_dto=dto)
