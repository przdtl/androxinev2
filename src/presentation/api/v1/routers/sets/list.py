from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from application.dto.sets.list_sets import ListSetsInputDTO
from application.use_cases.sets.list import ListSetsUseCase

from presentation.api.v1.schemas.common import CategorySchema
from presentation.api.v1.schemas.sets.list import ExerciseSchema
from presentation.api.v1.schemas.sets import ListSetsResponse
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.get(
    path="/",
    summary="Список сетов",
    description="Возвращает список сетов",
    response_description="Список сетов",
    response_model=Page[ListSetsResponse],
)
async def list_sets(
    uow: UowDep,
    params: Params = Depends(),
) -> Page[ListSetsResponse]:
    dto = ListSetsInputDTO(
        page=params.page,
        size=params.size,
    )
    use_case = ListSetsUseCase(uow=uow)
    sets = await use_case.execute(input_dto=dto)

    items = [
        ListSetsResponse(
            id=set_item.id,
            user_id=set_item.user_id,
            exercise=ExerciseSchema(
                id=set_item.exercise.id,
                title=set_item.exercise.title,
                short=set_item.exercise.short,
                category=CategorySchema(
                    id=set_item.exercise.category.id,
                    title=set_item.exercise.category.title,
                    created_at=set_item.exercise.category.created_at,
                    updated_at=set_item.exercise.category.updated_at,
                ),
                created_at=set_item.exercise.created_at,
                updated_at=set_item.exercise.updated_at,
                is_archived=set_item.exercise.is_archived,
            ),
            weight=set_item.weight,
            reps=set_item.reps,
            created_at=set_item.created_at,
        )
        for set_item in sets
    ]

    return paginate(items, params)
