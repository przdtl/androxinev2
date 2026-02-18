import uuid

from dto.template_exercises import (
    CreateTemplateExerciseInputDTO,
    CreateTemplateExerciseOutputDTO,
)
from models.templates import TemplateExercise


class CreateTemplateExerciseUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: CreateTemplateExerciseInputDTO,
    ) -> CreateTemplateExerciseOutputDTO:
        return CreateTemplateExerciseOutputDTO()
