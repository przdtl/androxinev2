from fastapi import APIRouter
from presentation.api.v1.schemas.sets import ListSetsResponse

router = APIRouter()


@router.get(
    path="/",
    summary="Список сетов",
    description="Возвращает список сетов",
    response_description="Список сетов",
    response_model=ListSetsResponse,
)
async def list_sets() -> ListSetsResponse:
    pass
