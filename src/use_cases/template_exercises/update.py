from dto.template_exercises import (
    UpdateTemplateExerciseInputDTO,
    UpdateTemplateExerciseOutputDTO,
)
from dto.template_exercises.update_template_exercise import (
    CategorySchema,
    ExerciseSchema,
)
from exceptions.exercises import ExerciseNotFoundError
from exceptions.templates import TemplateAccessDeniedError

from uow import UnitOfWork
from use_cases.templates._mapping import safe_datetime


class UpdateTemplateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateTemplateExerciseInputDTO,
    ) -> UpdateTemplateExerciseOutputDTO:
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

        updated = await self._uow.workout_templates_dao.update_exercise(
            template_id=input_dto.template_id,
            exercise_id=input_dto.exercise_id,
            default_weight=input_dto.default_weight,
            default_reps=input_dto.default_reps,
        )
        if updated is None:
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

        return UpdateTemplateExerciseOutputDTO(
            id=updated.id,
            default_weight=updated.weight,
            default_reps=updated.reps,
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
