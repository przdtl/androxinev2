import uuid

from fastapi import APIRouter, HTTPException

from dto.categories import DeleteCategoryInputDTO
from use_cases.categories import DeleteCategoryUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.categories import DeleteCategoryResponse

router = APIRouter()


@router.delete(
    path="/{id}/",
    summary="Удалить категорию",
    description="Удаляет категорию по идентификатору",
    response_description="Результат удаления",
    response_model=DeleteCategoryResponse,
)
async def delete_category(
    id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> DeleteCategoryResponse:
    dto = DeleteCategoryInputDTO(
        user_id=user_id,
        category_id=id,
    )
    use_case = DeleteCategoryUseCase(uow=uow)
    try:
        await use_case.execute(input_dto=dto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return DeleteCategoryResponse()
