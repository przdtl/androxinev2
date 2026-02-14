from application.dto.excercises import (
    RestoreExcerciseInputDTO,
    RestoreExcerciseOutputDTO,
)
from application.uow import UnitOfWork


class RestoreExcerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: RestoreExcerciseInputDTO,
    ) -> RestoreExcerciseOutputDTO:
        pass
