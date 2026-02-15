from typing import List

from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from application.dto.templates.get_today_templates import GetTodayTemplatesInputDTO
from application.use_cases.templates.get_today_templates import (
    GetTodayTemplatesUseCase,
)

from presentation.api.v1.schemas.common import (
    CategorySchema,
    DayOfWeek as DayOfWeekSchema,
)
from presentation.api.v1.schemas.templates import (
    GetTodayTemplatesResponse,
)
from presentation.api.v1.schemas.templates.get_today_templates import (
    TemplateExerciseSchema,
    ExerciseSchema,
)

from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.get(
    path="/today/",
    summary="Шаблоны тренировок на сегодня",
    description="Возвращает список шаблонов тренировок на сегодня",
    response_description="Список шаблонов тренировок на сегодня",
    response_model=Page[GetTodayTemplatesResponse],
)
async def get_today_templates(
    uow: UowDep,
    params: Params = Depends(),
) -> List[GetTodayTemplatesResponse]:
    dto = GetTodayTemplatesInputDTO()
    use_case = GetTodayTemplatesUseCase(uow=uow)
    templates = await use_case.execute(input_dto=dto)

    items = [
        GetTodayTemplatesResponse(
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
