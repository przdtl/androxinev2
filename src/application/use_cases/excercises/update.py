from application.dto.excercises import (
    UpdateExcerciseInputDTO,
    UpdateExcerciseOutputDTO,
)
from application.uow import UnitOfWork


class UpdateExcerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateExcerciseInputDTO,
    ) -> UpdateExcerciseOutputDTO:
        pass
