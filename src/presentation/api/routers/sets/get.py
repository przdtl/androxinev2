import uuid

from fastapi import APIRouter

from dto.sets import GetSetInputDTO
from use_cases.sets import GetSetUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.common import CategorySchema
from presentation.api.schemas.sets.get import ExerciseSchema
from presentation.api.schemas.sets import GetSetResponse

router = APIRouter()


@router.get(
    path="/{id}/",
    summary="Получить подход",
    description="Возвращает подход по идентификатору",
    response_description="Детали подхода",
    response_model=GetSetResponse,
)
async def get_set(
    id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> GetSetResponse:
    dto = GetSetInputDTO(
        user_id=user_id,
        set_id=id,
    )
    use_case = GetSetUseCase(uow=uow)
    set_item = await use_case.execute(input_dto=dto)

    return GetSetResponse(
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
    )
