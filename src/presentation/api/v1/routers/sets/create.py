from fastapi import APIRouter

from presentation.api.v1.schemas.sets import CreateSetRequest, CreateSetResponse

router = APIRouter()


@router.post(
    path="/",
    summary="Создать новый сет",
    description="Создает новый сет с указанными параметрами и возвращает его детали",
    response_description="Детали созданного сета",
    response_model=CreateSetResponse,
)
async def create_set(
    data: CreateSetRequest,
) -> CreateSetResponse:
    pass
