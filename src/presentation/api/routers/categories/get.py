import uuid

from fastapi import APIRouter, HTTPException

from dto.categories.get import GetCategoryInputDTO
from use_cases.categories.get import GetCategoryUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
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
    try:
        category = await use_case.execute(input_dto=dto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return GetCategoryResponse(
        id=category.id,
        title=category.title,
    )
