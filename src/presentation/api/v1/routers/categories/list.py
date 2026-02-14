from fastapi import APIRouter
from presentation.api.v1.schemas.categories import (
    ListCategoriesResponse,
)

router = APIRouter()


@router.get(
    path="/",
    summary="Список категорий",
    description="Возвращает список категорий",
    response_description="Список категорий",
    response_model=ListCategoriesResponse,
)
async def list_categories() -> ListCategoriesResponse:
    pass
