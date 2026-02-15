import uuid

from fastapi import APIRouter

from application.dto.sets.delete_set import DeleteSetInputDTO
from application.use_cases.sets.delete import DeleteSetUseCase

from presentation.api.v1.schemas.sets import DeleteSetRequest, DeleteSetResponse
from presentation.dependencies.uow import UowDep

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
    data: DeleteSetRequest,
    uow: UowDep,
) -> DeleteSetResponse:
    dto = DeleteSetInputDTO(id=id)
    use_case = DeleteSetUseCase(uow=uow)
    await use_case.execute(input_dto=dto)

    return DeleteSetResponse()
