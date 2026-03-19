from dto.template_exercises import (
    GetTemplateExerciseInputDTO,
    GetTemplateExerciseOutputDTO,
)
from dto.template_exercises.get_template_exercise import (
    CategorySchema,
    ExerciseSchema,
)
from exceptions.exercises import ExerciseNotFoundError
from exceptions.templates import TemplateAccessDeniedError

from uow import UnitOfWork
from use_cases.templates._mapping import safe_datetime


class GetTemplateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetTemplateExerciseInputDTO,
    ) -> GetTemplateExerciseOutputDTO:
        template = await self._uow.workout_templates_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            template_id=input_dto.template_id,
        )
        if template is None:
            raise TemplateAccessDeniedError(
                context={
                    "template_id": str(input_dto.template_id),
                    "user_id": str(input_dto.user_id),
                }
            )

        template_exercise = await self._uow.workout_templates_dao.get_exercise(
            template_id=input_dto.template_id,
            exercise_id=input_dto.exercise_id,
        )
        if template_exercise is None:
            raise ExerciseNotFoundError(
                context={"exercise_id": str(input_dto.exercise_id)}
            )

        exercise = await self._uow.exercises_dao.get_by_id(
            exercise_id=input_dto.exercise_id,
        )
        if exercise is None:
            raise ExerciseNotFoundError(
                context={"exercise_id": str(input_dto.exercise_id)}
            )

        return GetTemplateExerciseOutputDTO(
            id=template_exercise.id,
            default_weight=template_exercise.weight,
            default_reps=template_exercise.reps,
            order=template_exercise.order,
            exercise=ExerciseSchema(
                id=exercise.id,
                title=exercise.title,
                short=exercise.short,
                category=CategorySchema(
                    id=exercise.category.id,
                    title=exercise.category.title,
                    created_at=safe_datetime(
                        getattr(exercise.category, "created_at", None)
                    ),
                    updated_at=safe_datetime(
                        getattr(exercise.category, "updated_at", None)
                    ),
                ),
                created_at=safe_datetime(getattr(exercise, "created_at", None)),
                updated_at=safe_datetime(getattr(exercise, "updated_at", None)),
                is_archived=exercise.is_archived,
            ),
        )
