from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from dto.sets import ListSetsInputDTO
from use_cases.sets import ListSetsUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.common import CategorySchema
from presentation.api.schemas.sets.list import ExerciseSchema
from presentation.api.schemas.sets import ListSetsResponse

router = APIRouter()


@router.get(
    path="/",
    summary="Список сетов",
    description="Возвращает список сетов",
    response_description="Список сетов",
    response_model=Page[ListSetsResponse],
)
async def list_sets(
    uow: UOWDep,
    user_id: UserDep,
    params: Params = Depends(),
) -> Page[ListSetsResponse]:
    dto = ListSetsInputDTO(
        user_id=user_id,
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
                ),
                is_archived=set_item.exercise.is_archived,
            ),
            weight=set_item.weight,
            reps=set_item.reps,
            created_at=set_item.created_at,
        )
        for set_item in sets
    ]

    return paginate(items, params)
