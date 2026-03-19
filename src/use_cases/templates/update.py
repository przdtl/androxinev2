from dto.templates import (
    UpdateTemplateInputDTO,
    UpdateTemplateOutputDTO,
)
from dto.templates.update_template import (
    CategorySchema,
    ExerciseSchema,
    TemplateExerciseSchema,
    DayOfWeek,
)
from exceptions.templates import TemplateAccessDeniedError

from uow import UnitOfWork
from ._mapping import safe_datetime, safe_day_of_week


class UpdateTemplateUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateTemplateInputDTO,
    ) -> UpdateTemplateOutputDTO:
        template = await self._uow.workout_templates_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            template_id=input_dto.id,
        )
        if template is None:
            raise TemplateAccessDeniedError(
                context={
                    "template_id": str(input_dto.id),
                    "user_id": str(input_dto.user_id),
                }
            )

        updated_template = await self._uow.workout_templates_dao.update(
            template_id=input_dto.id,
            title=input_dto.title,
            day_of_week=(
                int(input_dto.day_of_week)
                if input_dto.day_of_week is not None
                else None
            ),
        )

        template_exercises = await self._uow.workout_templates_dao.list_exercises_all(
            template_id=updated_template.id,
        )
        exercises_payload: list[TemplateExerciseSchema] = []
        for item in template_exercises:
            exercise = await self._uow.exercises_dao.get_by_id(
                exercise_id=item.exercise_id,
            )
            if exercise is None:
                continue
            exercises_payload.append(
                TemplateExerciseSchema(
                    id=item.id,
                    default_weight=item.weight,
                    default_reps=item.reps,
                    order=item.order,
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

        return UpdateTemplateOutputDTO(
            id=updated_template.id,
            title=updated_template.title,
            day_of_week=DayOfWeek(safe_day_of_week(updated_template.day_of_week)),
            created_at=safe_datetime(getattr(updated_template, "created_at", None)),
            updated_at=safe_datetime(getattr(updated_template, "updated_at", None)),
            exercises=exercises_payload,
        )
