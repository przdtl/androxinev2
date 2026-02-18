import uuid
import datetime

from dto.exercises import (
    ArchiveExerciseInputDTO,
    ArchiveExerciseOutputDTO,
)
from dto.exercises.archive_excercise import CategorySchema


class ArchiveExerciseUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: ArchiveExerciseInputDTO,
    ) -> ArchiveExerciseOutputDTO:
        return ArchiveExerciseOutputDTO(
            id=input_dto.id,
            title="Exercise 1",
            short="Short description",
            category=CategorySchema(
                id=uuid.uuid4(),
                title="Category 1",
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            is_archived=True,
        )
