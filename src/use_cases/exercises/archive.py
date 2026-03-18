import uuid

from dto.exercises import (
    ArchiveExerciseInputDTO,
    ArchiveExerciseOutputDTO,
)
from dto.exercises.archive import CategorySchema

from uow import UnitOfWork
from common import utc_now_naive


class ArchiveExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

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
                created_at=utc_now_naive(),
                updated_at=utc_now_naive(),
            ),
            created_at=utc_now_naive(),
            updated_at=utc_now_naive(),
            is_archived=True,
        )
