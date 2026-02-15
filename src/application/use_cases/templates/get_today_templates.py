import datetime

from application.dto.templates import (
    GetTodayTemplatesInputDTO,
    GetTodayTemplatesOutputDTO,
)
from application.uow import UnitOfWork
from domain.enums import DayOfWeek


class GetTodayTemplatesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetTodayTemplatesInputDTO,
    ) -> list[GetTodayTemplatesOutputDTO]:
        today = datetime.datetime.now().weekday()
        templates = await self._uow.workout_templates_repo.list()

        result = []
        for template in templates:
            if template.day_of_week == today:
                exercises_output = []
                for tex in template.exercises:
                    exercise = await self._uow.exercises_repo.get(tex.exercise_id)
                    if exercise:
                        exercises_output.append(
                            {
                                "id": tex.id,
                                "default_weight": tex.default_weight,
                                "default_reps": tex.default_reps,
                                "order": tex.order,
                                "exercise": exercise,
                            }
                        )

                result.append(
                    GetTodayTemplatesOutputDTO(
                        id=template.id,
                        title=template.title,
                        day_of_week=template.day_of_week,
                        created_at=template.created_at,
                        updated_at=template.updated_at,
                        exercises=exercises_output,
                    )
                )
        return result
