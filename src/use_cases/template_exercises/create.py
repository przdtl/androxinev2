from dto.template_exercises import (
    CreateTemplateExerciseInputDTO,
    CreateTemplateExerciseOutputDTO,
)
from dto.template_exercises.create_template_exercise import (
    CategorySchema,
    ExerciseSchema,
)
from exceptions.exercises import ExerciseAccessDeniedError
from exceptions.templates import TemplateAccessDeniedError

from uow import UnitOfWork
from use_cases.templates._mapping import safe_datetime


class CreateTemplateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateTemplateExerciseInputDTO,
    ) -> CreateTemplateExerciseOutputDTO:
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

        exercise = await self._uow.exercises_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            exercise_id=input_dto.exercise_id,
        )
        if exercise is None:
            raise ExerciseAccessDeniedError(
                context={
                    "exercise_id": str(input_dto.exercise_id),
                    "user_id": str(input_dto.user_id),
                }
            )

        order = input_dto.order
        if order is None:
            order = await self._uow.workout_templates_dao.get_next_exercise_order(
                template_id=input_dto.template_id,
            )

        template_exercise = await self._uow.workout_templates_dao.create_exercise(
            template_id=input_dto.template_id,
            exercise_id=input_dto.exercise_id,
            default_weight=input_dto.default_weight,
            default_reps=input_dto.default_reps,
            order=order,
        )

        return CreateTemplateExerciseOutputDTO(
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
