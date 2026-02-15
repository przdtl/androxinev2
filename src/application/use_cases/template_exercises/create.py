import uuid

from application.dto.template_exercises import (
    CreateTemplateExerciseInputDTO,
    CreateTemplateExerciseOutputDTO,
)
from application.uow import UnitOfWork
from domain.entities.templates import TemplateExercise


class CreateTemplateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateTemplateExerciseInputDTO,
    ) -> CreateTemplateExerciseOutputDTO:
        exercise = await self._uow.exercises_repo.get(input_dto.exercise_id)
        if not exercise:
            raise ValueError(f"Exercise {input_dto.exercise_id} not found")

        template_exercise = TemplateExercise(
            id=uuid.uuid4(),
            exercise_id=input_dto.exercise_id,
            weight=input_dto.default_weight,
            reps=input_dto.default_reps,
            order=input_dto.order,
        )

        # In real implementation, add to template
        await self._uow.commit()

        return CreateTemplateExerciseOutputDTO(
            id=template_exercise.id,
            default_weight=template_exercise.default_weight,
            default_reps=template_exercise.default_reps,
            order=template_exercise.order,
            exercise=exercise,
        )
