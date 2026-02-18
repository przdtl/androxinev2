import uuid
import datetime

from dto.sets import (
    CreateSetInputDTO,
    CreateSetOutputDTO,
)
from dto.sets.create_set import ExerciseSchema, CategorySchema
from models.sets import Set


class CreateSetUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: CreateSetInputDTO,
    ) -> CreateSetOutputDTO:
        return CreateSetOutputDTO()
