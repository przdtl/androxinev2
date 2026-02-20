from fastapi import APIRouter

from dto.templates.create_template import (
    CreateTemplateInputDTO,
    TemplateExerciseCreateInput,
)
from dto.templates.create_template import DayOfWeek as DayOfWeekDTO
from use_cases.templates.create import CreateTemplateUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.common import (
    CategorySchema,
    DayOfWeek as DayOfWeekSchema,
)
from presentation.api.schemas.templates import (
    CreateTemplateRequest,
    CreateTemplateResponse,
)
from presentation.api.schemas.templates.create import (
    TemplateExerciseSchema,
    ExerciseSchema,
)

router = APIRouter()


@router.post(
    path="/",
    summary="Создать шаблон тренировки",
    description="Создает новый шаблон тренировки",
    response_description="Детали созданного шаблона",
    response_model=CreateTemplateResponse,
)
async def create_template(
    data: CreateTemplateRequest,
    uow: UOWDep,
    user_id: UserDep,
) -> CreateTemplateResponse:
    dto = CreateTemplateInputDTO(
        title=data.title,
        day_of_week=DayOfWeekDTO(data.day_of_week),
        exercises=[
            TemplateExerciseCreateInput(
                exercise_id=item.exercise_id,
                default_weight=item.default_weight,
                default_reps=item.default_reps,
                order=item.order,
            )
            for item in data.exercises
        ],
    )
    use_case = CreateTemplateUseCase(uow=uow)
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

    return CreateTemplateResponse(
        id=template.id,
        title=template.title,
        day_of_week=DayOfWeekSchema(template.day_of_week),
        created_at=template.created_at,
        updated_at=template.updated_at,
        exercises=exercises,
    )
