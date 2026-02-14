from application.dto.excercises import (
    ArchiveExcerciseInputDTO,
    ArchiveExcerciseOutputDTO,
)
from application.uow import UnitOfWork


class ArchiveExcerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ArchiveExcerciseInputDTO,
    ) -> ArchiveExcerciseOutputDTO:
        pass
