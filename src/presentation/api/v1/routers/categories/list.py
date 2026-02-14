from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from presentation.api.v1.schemas.categories import (
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
    params: Params = Depends(),
) -> Page[ListCategoriesResponse]:
    pass
