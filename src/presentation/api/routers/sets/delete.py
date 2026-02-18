import uuid

from fastapi import APIRouter

from dto.sets.delete_set import DeleteSetInputDTO
from use_cases.sets.delete import DeleteSetUseCase

from ..schemas.sets import DeleteSetResponse

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
) -> DeleteSetResponse:
    dto = DeleteSetInputDTO(id=id)
    use_case = DeleteSetUseCase()
    await use_case.execute(input_dto=dto)

    return DeleteSetResponse()
