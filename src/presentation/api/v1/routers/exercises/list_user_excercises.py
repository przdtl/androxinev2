from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from application.dto.exercises.list_user_excercises import (
    ListUserExercisesInputDTO,
)
from application.use_cases.exercises.list_user_excercises import (
    ListUserExercisesUseCase,
)

from presentation.api.v1.schemas.common import CategorySchema
from presentation.api.v1.schemas.exercises import (
    ListUserExercisesResponse,
)
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.get(
    path="/user/",
    summary="Список упражнений пользователя",
    description="Возвращает список упражнений пользователя",
    response_description="Список упражнений пользователя",
    response_model=Page[ListUserExercisesResponse],
)
async def list_user_excercises(
    uow: UowDep,
    params: Params = Depends(),
) -> Page[ListUserExercisesResponse]:
    dto = ListUserExercisesInputDTO(
        page=params.page,
        size=params.size,
    )
    use_case = ListUserExercisesUseCase(uow=uow)
    exercises = await use_case.execute(input_dto=dto)

    items = [
        ListUserExercisesResponse(
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
