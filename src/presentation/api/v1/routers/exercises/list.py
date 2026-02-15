from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from application.dto.exercises.list_excercises import ListExercisesInputDTO
from application.use_cases.exercises.list import ListExercisesUseCase

from presentation.api.v1.schemas.common import CategorySchema
from presentation.api.v1.schemas.exercises import (
    ListExercisesResponse,
)
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.get(
    path="/",
    summary="Список упражнений",
    description="Возвращает список упражнений",
    response_description="Список упражнений",
    response_model=Page[ListExercisesResponse],
)
async def list_excercises(
    uow: UowDep,
    params: Params = Depends(),
) -> Page[ListExercisesResponse]:
    dto = ListExercisesInputDTO(
        page=params.page,
        size=params.size,
    )
    use_case = ListExercisesUseCase(uow=uow)
    exercises = await use_case.execute(input_dto=dto)

    items = [
        ListExercisesResponse(
            id=exercise.id,
            title=exercise.title,
            short=exercise.short,
            category=CategorySchema(
                id=exercise.category.id,
                title=exercise.category.title,
                created_at=exercise.category.created_at,
                updated_at=exercise.category.updated_at,
            ),
            created_at=exercise.created_at,
            updated_at=exercise.updated_at,
            is_archived=exercise.is_archived,
        )
        for exercise in exercises
    ]

    return paginate(items, params)
