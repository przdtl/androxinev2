import uuid

from dto.exercises import (
    RestoreExerciseInputDTO,
    RestoreExerciseOutputDTO,
)
from dto.exercises.restore import CategorySchema

from uow import UnitOfWork
from common import utc_now_naive


class RestoreExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: RestoreExerciseInputDTO,
    ) -> RestoreExerciseOutputDTO:
        return RestoreExerciseOutputDTO(
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
            is_archived=False,
        )
