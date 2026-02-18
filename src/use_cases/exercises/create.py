import uuid
import datetime

from dto.exercises import (
    CreateExerciseInputDTO,
    CreateExerciseOutputDTO,
)
from dto.exercises.create_excercise import CategorySchema


class CreateExerciseUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: CreateExerciseInputDTO,
    ) -> CreateExerciseOutputDTO:
        return CreateExerciseOutputDTO(
            id=uuid.uuid4(),
            title=input_dto.title,
            short=input_dto.short,
            category=CategorySchema(
                id=input_dto.category_id,
                title="Category 1",
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            is_archived=False,
        )
