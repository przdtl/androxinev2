import uuid

from fastapi import APIRouter, HTTPException

from dto.categories.update import UpdateCategoryInputDTO
from use_cases.categories.update import UpdateCategoryUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.categories import (
    UpdateCategoryRequest,
    UpdateCategoryResponse,
)


router = APIRouter()


@router.patch(
    path="/{id}/",
    summary="Обновить категорию",
    description="Обновляет категорию по идентификатору",
    response_description="Обновленные детали категории",
    response_model=UpdateCategoryResponse,
)
async def update_category(
    id: uuid.UUID,
    data: UpdateCategoryRequest,
    uow: UOWDep,
    user_id: UserDep,
) -> UpdateCategoryResponse:
    dto = UpdateCategoryInputDTO(
        user_id=user_id,
        category_id=id,
        title=data.title,
    )
    use_case = UpdateCategoryUseCase(uow=uow)
    try:
        category = await use_case.execute(input_dto=dto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return UpdateCategoryResponse(
        id=category.id,
        title=category.title,
    )
