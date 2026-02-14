from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from presentation.api.v1.schemas.template_exercises import (
    ListTemplateExercisesResponse,
)

router = APIRouter()


@router.get(
    path="/",
    summary="Список упражнений в шаблоне",
    description="Возвращает список упражнений в шаблоне",
    response_description="Список упражнений в шаблоне",
    response_model=Page[ListTemplateExercisesResponse],
)
async def list_template_excercises(
    params: Params = Depends(),
) -> Page[ListTemplateExercisesResponse]:
    pass
