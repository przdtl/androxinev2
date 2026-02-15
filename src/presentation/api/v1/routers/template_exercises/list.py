from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params

from application.dto.template_exercises.list_template_exercises import (
    ListTemplateExercisesInputDTO,
)
from application.use_cases.template_exercises.list import (
    ListTemplateExercisesUseCase,
)
from presentation.api.v1.schemas.common import CategorySchema
from presentation.api.v1.schemas.template_exercises.list import ExerciseSchema
from presentation.api.v1.schemas.template_exercises import (
    ListTemplateExercisesResponse,
)
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.get(
    path="/",
    summary="Список упражнений в шаблоне",
    description="Возвращает список упражнений в шаблоне",
    response_description="Список упражнений в шаблоне",
    response_model=Page[ListTemplateExercisesResponse],
)
async def list_template_excercises(
    uow: UowDep,
    params: Params = Depends(),
) -> Page[ListTemplateExercisesResponse]:
    dto = ListTemplateExercisesInputDTO(
        page=params.page,
        size=params.size,
    )
    use_case = ListTemplateExercisesUseCase(uow=uow)
    template_exercises = await use_case.execute(input_dto=dto)

    items = [
        ListTemplateExercisesResponse(
            id=template_exercise.id,
            default_weight=template_exercise.default_weight,
            default_reps=template_exercise.default_reps,
            order=template_exercise.order,
            exercise=ExerciseSchema(
                id=template_exercise.exercise.id,
                title=template_exercise.exercise.title,
                short=template_exercise.exercise.short,
                category=CategorySchema(
                    id=template_exercise.exercise.category.id,
                    title=template_exercise.exercise.category.title,
                    created_at=template_exercise.exercise.category.created_at,
                    updated_at=template_exercise.exercise.category.updated_at,
                ),
                created_at=template_exercise.exercise.created_at,
                updated_at=template_exercise.exercise.updated_at,
                is_archived=template_exercise.exercise.is_archived,
            ),
        )
        for template_exercise in template_exercises
    ]

    return paginate(items, params)
