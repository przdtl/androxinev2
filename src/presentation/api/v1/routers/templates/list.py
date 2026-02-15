from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from application.dto.templates.list_templates import ListTemplatesInputDTO
from application.use_cases.templates.list import ListTemplatesUseCase

from presentation.api.v1.schemas.common import (
    CategorySchema,
    DayOfWeek as DayOfWeekSchema,
)
from presentation.api.v1.schemas.templates import (
    ListTemplatesResponse,
)
from presentation.api.v1.schemas.templates.list import (
    TemplateExerciseSchema,
    ExerciseSchema,
)
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.get(
    path="/",
    summary="Список шаблонов тренировок",
    description="Возвращает список шаблонов тренировок",
    response_description="Список шаблонов тренировок",
    response_model=Page[ListTemplatesResponse],
)
async def list_templates(
    uow: UowDep,
    params: Params = Depends(),
) -> Page[ListTemplatesResponse]:
    dto = ListTemplatesInputDTO(
        page=params.page,
        size=params.size,
    )
    use_case = ListTemplatesUseCase(uow=uow)
    templates = await use_case.execute(input_dto=dto)

    items = [
        ListTemplatesResponse(
            id=template.id,
            title=template.title,
            day_of_week=DayOfWeekSchema(template.day_of_week),
            created_at=template.created_at,
            updated_at=template.updated_at,
            exercises=[
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
            ],
        )
        for template in templates
    ]

    return paginate(items, params)
