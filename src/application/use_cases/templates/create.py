import uuid
import datetime

from application.dto.templates import (
    CreateTemplateInputDTO,
    CreateTemplateOutputDTO,
)
from application.uow import UnitOfWork
from domain.entities.templates import WorkoutTemplate, TemplateExercise


class CreateTemplateUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateTemplateInputDTO,
    ) -> CreateTemplateOutputDTO:
        async with self._uow:
            template_exercises = []
            for ex_input in input_dto.exercises:
                exercise = await self._uow.exercises_repo.get(ex_input.exercise_id)
                if not exercise:
                    raise ValueError(f"Exercise {ex_input.exercise_id} not found")

                template_exercises.append(
                    TemplateExercise(
                        id=uuid.uuid4(),
                        exercise_id=ex_input.exercise_id,
                        weight=ex_input.default_weight,
                        reps=ex_input.default_reps,
                        order=ex_input.order,
                    )
                )

            now = datetime.datetime.now()
            template = WorkoutTemplate(
                id=uuid.uuid4(),
                user_id=1,  # TODO: get from context
                title=input_dto.title,
                day_of_week=input_dto.day_of_week,
                created_at=now,
                updated_at=now,
                exercises=template_exercises,
            )

            await self._uow.workout_templates_repo.add(template)
            await self._uow.commit()

            # Build output with exercises
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

            return CreateTemplateOutputDTO(
                id=template.id,
                title=template.title,
                day_of_week=template.day_of_week,
                created_at=template.created_at,
                updated_at=template.updated_at,
                exercises=exercises_output,
            )
