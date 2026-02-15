import uuid

from fastapi import APIRouter

from application.dto.template_exercises.update_template_exercise import (
    UpdateTemplateExerciseInputDTO,
)
from application.use_cases.template_exercises.update import (
    UpdateTemplateExerciseUseCase,
)

from presentation.api.v1.schemas.common import CategorySchema
from presentation.api.v1.schemas.template_exercises.update import ExerciseSchema
from presentation.api.v1.schemas.template_exercises import (
    UpdateTemplateExerciseRequest,
    UpdateTemplateExerciseResponse,
)
from presentation.dependencies.uow import UowDep

router = APIRouter()


@router.patch(
    path="/{id}/",
    summary="Обновить упражнение в шаблоне",
    description="Обновляет упражнение в шаблоне по идентификатору",
    response_description="Обновленные детали упражнения в шаблоне",
    response_model=UpdateTemplateExerciseResponse,
)
async def update_template_excercise(
    id: uuid.UUID,
    data: UpdateTemplateExerciseRequest,
    uow: UowDep,
) -> UpdateTemplateExerciseResponse:
    dto = UpdateTemplateExerciseInputDTO(
        id=id,
        default_weight=data.default_weight,
        default_reps=data.default_reps,
        order=data.order,
    )
    use_case = UpdateTemplateExerciseUseCase(uow=uow)
    template_exercise = await use_case.execute(input_dto=dto)

    return UpdateTemplateExerciseResponse(
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
