from fastapi import APIRouter

from application.dto.sets.create_set import CreateSetInputDTO
from application.use_cases.sets.create import CreateSetUseCase

from presentation.api.v1.schemas.common import CategorySchema
from presentation.api.v1.schemas.sets.create import ExerciseSchema
from presentation.api.v1.schemas.sets import CreateSetRequest, CreateSetResponse
from presentation.dependencies.uow import UowDep

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
    uow: UowDep,
) -> CreateSetResponse:
    dto = CreateSetInputDTO(
        exercise_id=data.exercise_id,
        weight=data.weight,
        reps=data.reps,
    )
    use_case = CreateSetUseCase(uow=uow)
    set_item = await use_case.execute(input_dto=dto)

    return CreateSetResponse(
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
