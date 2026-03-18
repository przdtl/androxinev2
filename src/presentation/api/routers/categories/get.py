import uuid

from fastapi import APIRouter

from dto.categories.get import GetCategoryInputDTO
from use_cases.categories.get import GetCategoryUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.responses.categories import GET_CATEGORY_RESPONSES
from presentation.api.schemas.categories import (
    GetCategoryResponse,
)


router = APIRouter()


@router.get(
    path="/{id}/",
    summary="Получить категорию",
    description="Возвращает категорию по идентификатору",
    response_description="Детали категории",
    response_model=GetCategoryResponse,
    responses=GET_CATEGORY_RESPONSES,
)
async def get_category(
    id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> GetCategoryResponse:
    dto = GetCategoryInputDTO(
        user_id=user_id,
        category_id=id,
    )
    use_case = GetCategoryUseCase(uow=uow)
    category = await use_case.execute(input_dto=dto)

    return GetCategoryResponse(
        id=category.id,
        title=category.title,
    )
