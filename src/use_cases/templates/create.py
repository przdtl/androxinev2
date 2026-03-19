from dto.templates import (
    CreateTemplateInputDTO,
    CreateTemplateOutputDTO,
)
from dto.templates.create_template import (
    CategorySchema,
    ExerciseSchema,
    TemplateExerciseSchema,
    DayOfWeek,
)
from exceptions.exercises import ExerciseAccessDeniedError

from uow import UnitOfWork
from ._mapping import safe_datetime, safe_day_of_week


class CreateTemplateUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateTemplateInputDTO,
    ) -> CreateTemplateOutputDTO:
        template = await self._uow.workout_templates_dao.create(
            user_id=input_dto.user_id,
            title=input_dto.title,
            day_of_week=(
                int(input_dto.day_of_week)
                if input_dto.day_of_week is not None
                else None
            ),
        )

        exercises_payload: list[TemplateExerciseSchema] = []
        for index, item in enumerate(input_dto.exercises):
            exercise = await self._uow.exercises_dao.get_by_user_and_id(
                user_id=input_dto.user_id,
                exercise_id=item.exercise_id,
            )
            if exercise is None:
                raise ExerciseAccessDeniedError(
                    context={
                        "exercise_id": str(item.exercise_id),
                        "user_id": str(input_dto.user_id),
                    }
                )

            order = item.order
            if order is None:
                order = await self._uow.workout_templates_dao.get_next_exercise_order(
                    template_id=template.id,
                )
                if order < index:
                    order = index

            template_exercise = await self._uow.workout_templates_dao.create_exercise(
                template_id=template.id,
                exercise_id=item.exercise_id,
                default_weight=item.default_weight,
                default_reps=item.default_reps,
                order=order,
            )

            exercises_payload.append(
                TemplateExerciseSchema(
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
            )

        return CreateTemplateOutputDTO(
            id=template.id,
            title=template.title,
            day_of_week=DayOfWeek(safe_day_of_week(template.day_of_week)),
            created_at=safe_datetime(getattr(template, "created_at", None)),
            updated_at=safe_datetime(getattr(template, "updated_at", None)),
            exercises=exercises_payload,
        )
