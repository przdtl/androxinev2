from application.dto.exercises import (
    ArchiveExerciseInputDTO,
    ArchiveExerciseOutputDTO,
)
from application.uow import UnitOfWork


class ArchiveExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ArchiveExerciseInputDTO,
    ) -> ArchiveExerciseOutputDTO:
        pass
