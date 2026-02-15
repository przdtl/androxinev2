from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from application.dto.categories.list_categories import ListCategoriesInputDTO
from application.use_cases.categories.list import ListCategoriesUseCase

from presentation.api.v1.schemas.categories import (
    ListCategoriesResponse,
)
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.get(
    path="/",
    summary="Список категорий",
    description="Возвращает список категорий",
    response_description="Список категорий",
    response_model=Page[ListCategoriesResponse],
)
async def list_categories(
    uow: UowDep,
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
