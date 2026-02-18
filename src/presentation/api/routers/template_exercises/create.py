from fastapi import APIRouter

from dto.template_exercises.create_template_exercise import (
    CreateTemplateExerciseInputDTO,
)
from use_cases.template_exercises.create import (
    CreateTemplateExerciseUseCase,
)

from ..schemas.common import CategorySchema
from ..schemas.template_exercises.create import ExerciseSchema
from ..schemas.template_exercises import (
    CreateTemplateExerciseRequest,
    CreateTemplateExerciseResponse,
)

router = APIRouter()


@router.post(
    path="/",
    summary="Добавить упражнение в шаблон",
    description="Добавляет упражнение в шаблон тренировок",
    response_description="Детали упражнения в шаблоне",
    response_model=CreateTemplateExerciseResponse,
)
async def create_template_exercise(
    data: CreateTemplateExerciseRequest,
) -> CreateTemplateExerciseResponse:
    dto = CreateTemplateExerciseInputDTO(
        exercise_id=data.exercise_id,
        default_weight=data.default_weight,
        default_reps=data.default_reps,
        order=data.order,
    )
    use_case = CreateTemplateExerciseUseCase()
    template_exercise = await use_case.execute(input_dto=dto)

    return CreateTemplateExerciseResponse(
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
