import uuid

from fastapi import APIRouter

from dto.sets import UpdateSetInputDTO
from use_cases.sets import UpdateSetUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.responses.sets.update import UPDATE_SET_RESPONSES
from presentation.api.schemas.common import CategorySchema
from presentation.api.schemas.sets.update import ExerciseSchema
from presentation.api.schemas.sets import UpdateSetRequest, UpdateSetResponse

router = APIRouter()


@router.patch(
    path="/{set_id}/",
    summary="Обновить подход",
    description="Обновляет подход по идентификатору",
    response_description="Обновленные детали подхода",
    response_model=UpdateSetResponse,
    responses=UPDATE_SET_RESPONSES,
)
async def update_set(
    set_id: uuid.UUID,
    data: UpdateSetRequest,
    uow: UOWDep,
    user_id: UserDep,
) -> UpdateSetResponse:
    dto = UpdateSetInputDTO(
        user_id=user_id,
        set_id=set_id,
        weight=data.weight,
        reps=data.reps,
    )
    use_case = UpdateSetUseCase(uow=uow)
    set_item = await use_case.execute(input_dto=dto)

    return UpdateSetResponse(
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
