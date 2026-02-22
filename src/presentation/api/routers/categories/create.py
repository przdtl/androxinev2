from fastapi import APIRouter

from dto.categories.create import CreateCategoryInputDTO
from use_cases.categories.create import CreateCategoryUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.categories import (
    CreateCategoryRequest,
    CreateCategoryResponse,
)


router = APIRouter()


@router.post(
    path="/",
    summary="Создать категорию",
    description="Создает новую категорию",
    response_description="Детали созданной категории",
    response_model=CreateCategoryResponse,
)
async def create_category(
    data: CreateCategoryRequest,
    uow: UOWDep,
    user_id: UserDep,
) -> CreateCategoryResponse:
    dto = CreateCategoryInputDTO(
        user_id=user_id,
        title=data.title,
    )
    use_case = CreateCategoryUseCase(uow=uow)
    category = await use_case.execute(input_dto=dto)

    return CreateCategoryResponse(
        id=category.id,
        title=category.title,
    )
