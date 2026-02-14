from fastapi import APIRouter
from presentation.api.v1.schemas.sets import DeleteSetRequest, DeleteSetResponse

router = APIRouter()


@router.delete(
    path="/{id}/",
    summary="Удалить сет",
    description="Удаляет сет по идентификатору",
    response_description="Результат удаления",
    response_model=DeleteSetResponse,
)
async def delete_set(
    data: DeleteSetRequest,
) -> DeleteSetResponse:
    pass
