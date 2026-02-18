import uuid
import datetime

from dto.exercises import (
    ListExercisesInputDTO,
    ListExercisesOutputDTO,
)
from dto.exercises.list_excercises import CategorySchema


class ListExercisesUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: ListExercisesInputDTO,
    ) -> list[ListExercisesOutputDTO]:
        return [
            ListExercisesOutputDTO(
                id=uuid.uuid4(),
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
                is_archived=False,
            )
        ]
