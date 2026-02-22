from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params
import uuid

from dto.exercises import ListExercisesInputDTO
from use_cases.exercises import ListExercisesUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.exercises import (
    ListExercisesResponse,
)

router = APIRouter()


@router.get(
    path="/",
    summary="Список упражнений",
    description="Возвращает список упражнений",
    response_description="Список упражнений",
    response_model=Page[ListExercisesResponse],
)
async def list_excercises(
    uow: UOWDep,
    user_id: UserDep,
    category_id: uuid.UUID | None = None,
    params: Params = Depends(),
) -> Page[ListExercisesResponse]:
    dto = ListExercisesInputDTO(
        user_id=user_id,
        page=params.page,
        size=params.size,
        category_id=category_id,
    )
    use_case = ListExercisesUseCase(uow=uow)
    exercises = await use_case.execute(input_dto=dto)

    return Page.create(items=exercises, total=len(exercises), params=params)
