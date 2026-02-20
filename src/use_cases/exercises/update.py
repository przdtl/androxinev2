import uuid
import datetime

from dto.exercises import (
    UpdateExerciseInputDTO,
    UpdateExerciseOutputDTO,
)
from dto.exercises.update_excercise import CategorySchema

from uow import UnitOfWork


class UpdateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateExerciseInputDTO,
    ) -> UpdateExerciseOutputDTO:
        return UpdateExerciseOutputDTO(
            id=input_dto.id,
            title=input_dto.title or "Exercise 1",
            short=input_dto.short or "Short description",
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
