import uuid

from fastapi import APIRouter

from dto.categories.update import UpdateCategoryInputDTO
from use_cases.categories.update import UpdateCategoryUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.responses.categories import UPDATE_CATEGORY_RESPONSES
from presentation.api.schemas.categories import (
    UpdateCategoryRequest,
    UpdateCategoryResponse,
)


router = APIRouter()


@router.patch(
    path="/{category_id}/",
    summary="Обновить категорию",
    description="Обновляет категорию по идентификатору",
    response_description="Обновленные детали категории",
    response_model=UpdateCategoryResponse,
    responses=UPDATE_CATEGORY_RESPONSES,
)
async def update_category(
    category_id: uuid.UUID,
    data: UpdateCategoryRequest,
    uow: UOWDep,
    user_id: UserDep,
) -> UpdateCategoryResponse:
    dto = UpdateCategoryInputDTO(
        user_id=user_id,
        category_id=category_id,
        title=data.title,
    )
    use_case = UpdateCategoryUseCase(uow=uow)
    category = await use_case.execute(input_dto=dto)

    return UpdateCategoryResponse(
        id=category.id,
        title=category.title,
    )
