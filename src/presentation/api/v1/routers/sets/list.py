from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from presentation.api.v1.schemas.sets import ListSetsResponse

router = APIRouter()


@router.get(
    path="/",
    summary="Список сетов",
    description="Возвращает список сетов",
    response_description="Список сетов",
    response_model=Page[ListSetsResponse],
)
async def list_sets(
    params: Params = Depends(),
) -> Page[ListSetsResponse]:
    pass
