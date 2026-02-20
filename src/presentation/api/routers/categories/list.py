from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from dto.categories.list_categories import ListCategoriesInputDTO

from use_cases.categories.list import ListCategoriesUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.categories import (
    ListCategoriesResponse,
)

router = APIRouter()


@router.get(
    path="/",
    summary="Список категорий",
    description="Возвращает список категорий",
    response_description="Список категорий",
    response_model=Page[ListCategoriesResponse],
)
async def list_categories(
    uow: UOWDep,
    user_id: UserDep,
    params: Params = Depends(),
) -> Page[ListCategoriesResponse]:
    dto = ListCategoriesInputDTO(
        page=params.page,
        size=params.size,
    )
    use_case = ListCategoriesUseCase(uow=uow)
    categories = await use_case.execute(input_dto=dto)

    items = [
        ListCategoriesResponse(
            id=category.id,
            title=category.title,
            created_at=category.created_at,
            updated_at=category.updated_at,
        )
        for category in categories
    ]

    return paginate(items, params)
