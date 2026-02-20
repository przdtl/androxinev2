import uuid

from fastapi import APIRouter

from dto.templates.update_template import (
    UpdateTemplateInputDTO,
    DayOfWeek as DayOfWeekDTO,
)
from use_cases.templates.update import UpdateTemplateUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.common import (
    CategorySchema,
    DayOfWeek as DayOfWeekSchema,
)
from presentation.api.schemas.templates import (
    UpdateTemplateRequest,
    UpdateTemplateResponse,
)
from presentation.api.schemas.templates.update import (
    TemplateExerciseSchema,
    ExerciseSchema,
)

router = APIRouter()


@router.patch(
    path="/{id}/",
    summary="Обновить шаблон тренировки",
    description="Обновляет шаблон тренировки по идентификатору",
    response_description="Обновленные детали шаблона",
    response_model=UpdateTemplateResponse,
)
async def update_template(
    id: uuid.UUID,
    data: UpdateTemplateRequest,
    uow: UOWDep,
    user_id: UserDep,
) -> UpdateTemplateResponse:
    dto = UpdateTemplateInputDTO(
        id=id,
        title=data.title,
        day_of_week=DayOfWeekDTO(data.day_of_week),
    )
    use_case = UpdateTemplateUseCase(uow=uow)
    template = await use_case.execute(input_dto=dto)

    exercises = [
        TemplateExerciseSchema(
            id=exc.id,
            default_weight=exc.default_weight,
            default_reps=exc.default_reps,
            order=exc.order,
            exercise=ExerciseSchema(
                id=exc.exercise.id,
                title=exc.exercise.title,
                short=exc.exercise.short,
                category=CategorySchema(
                    id=exc.exercise.category.id,
                    title=exc.exercise.category.title,
                    created_at=exc.exercise.category.created_at,
                    updated_at=exc.exercise.category.updated_at,
                ),
                created_at=exc.exercise.created_at,
                updated_at=exc.exercise.updated_at,
                is_archived=exc.exercise.is_archived,
            ),
        )
        for exc in template.exercises
    ]

    return UpdateTemplateResponse(
        id=template.id,
        title=template.title,
        day_of_week=DayOfWeekSchema(template.day_of_week),
        created_at=template.created_at,
        updated_at=template.updated_at,
        exercises=exercises,
    )
