import uuid

from fastapi import APIRouter

from dto.templates import (
    GetTemplateInputDTO,
    GetTemplateOutputDTO,
)
from use_cases.templates.get import GetTemplateUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.common import (
    CategorySchema,
    DayOfWeek as DayOfWeekSchema,
)
from presentation.api.schemas.templates.get import (
    TemplateExerciseSchema,
    ExerciseSchema,
    TemplateResponse,
)

router = APIRouter()


@router.get(
    path="/{template_id}/",
    summary="Получить шаблон тренировки",
    description="Возвращает детали шаблона тренировки по идентификатору",
    response_description="Детали шаблона тренировки",
    response_model=TemplateResponse,
)
async def get_template(
    template_id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> TemplateResponse:
    dto = GetTemplateInputDTO(user_id=user_id, id=template_id)
    use_case = GetTemplateUseCase(uow=uow)
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
                ),
                created_at=exc.exercise.created_at,
                updated_at=exc.exercise.updated_at,
                is_archived=exc.exercise.is_archived,
            ),
        )
        for exc in template.exercises
    ]

    return TemplateResponse(
        id=template.id,
        title=template.title,
        day_of_week=DayOfWeekSchema(template.day_of_week),
        created_at=template.created_at,
        updated_at=template.updated_at,
        exercises=exercises,
    )
