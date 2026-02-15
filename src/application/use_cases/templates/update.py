import datetime

from application.dto.templates import (
    UpdateTemplateInputDTO,
    UpdateTemplateOutputDTO,
)
from application.uow import UnitOfWork


class UpdateTemplateUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateTemplateInputDTO,
    ) -> UpdateTemplateOutputDTO:
        template = await self._uow.workout_templates_repo.get(input_dto.id)
        if not template:
            raise ValueError(f"Template {input_dto.id} not found")

        # Update fields - in real implementation update mutable fields
        await self._uow.commit()

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

        return UpdateTemplateOutputDTO(
            id=template.id,
            title=input_dto.title if input_dto.title else template.title,
            day_of_week=(
                input_dto.day_of_week
                if input_dto.day_of_week is not None
                else template.day_of_week
            ),
            created_at=template.created_at,
            updated_at=datetime.datetime.now(),
            exercises=exercises_output,
        )
