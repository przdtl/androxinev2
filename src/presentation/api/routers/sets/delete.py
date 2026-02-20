import uuid

from fastapi import APIRouter

from dto.sets.delete_set import DeleteSetInputDTO
from use_cases.sets.delete import DeleteSetUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.sets import DeleteSetResponse

router = APIRouter()


@router.delete(
    path="/{id}/",
    summary="Удалить сет",
    description="Удаляет сет по идентификатору",
    response_description="Результат удаления",
    response_model=DeleteSetResponse,
)
async def delete_set(
    id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> DeleteSetResponse:
    dto = DeleteSetInputDTO(id=id)
    use_case = DeleteSetUseCase(uow=uow)
    await use_case.execute(input_dto=dto)

    return DeleteSetResponse()
