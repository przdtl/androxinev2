from dto.templates import (
    ListTemplatesInputDTO,
    ListTemplatesOutputDTO,
)
from dto.templates.list_templates import (
    CategorySchema,
    ExerciseSchema,
    TemplateExerciseSchema,
    DayOfWeek,
)

from uow import UnitOfWork
from ._mapping import safe_datetime, safe_day_of_week


class ListTemplatesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListTemplatesInputDTO,
    ) -> list[ListTemplatesOutputDTO]:
        templates = await self._uow.workout_templates_dao.list_by_user_id(
            user_id=input_dto.user_id,
            page=input_dto.page,
            size=input_dto.size,
        )

        result: list[ListTemplatesOutputDTO] = []
        for template in templates:
            template_exercises = (
                await self._uow.workout_templates_dao.list_exercises_all(
                    template_id=template.id,
                )
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
                            created_at=safe_datetime(
                                getattr(exercise, "created_at", None)
                            ),
                            updated_at=safe_datetime(
                                getattr(exercise, "updated_at", None)
                            ),
                            is_archived=exercise.is_archived,
                        ),
                    )
                )

            result.append(
                ListTemplatesOutputDTO(
                    id=template.id,
                    title=template.title,
                    day_of_week=DayOfWeek(safe_day_of_week(template.day_of_week)),
                    created_at=safe_datetime(getattr(template, "created_at", None)),
                    updated_at=safe_datetime(getattr(template, "updated_at", None)),
                    exercises=exercises_payload,
                )
            )

        return result
