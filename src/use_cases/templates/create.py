import uuid
import datetime

from dto.templates import (
    CreateTemplateInputDTO,
    CreateTemplateOutputDTO,
)
from models.templates import WorkoutTemplate, TemplateExercise


class CreateTemplateUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: CreateTemplateInputDTO,
    ) -> CreateTemplateOutputDTO:
        return CreateTemplateOutputDTO()
