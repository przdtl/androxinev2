from application.dto.excercises import (
    GetExcerciseInputDTO,
    GetExcerciseOutputDTO,
)
from application.uow import UnitOfWork


class GetExcerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetExcerciseInputDTO,
    ) -> GetExcerciseOutputDTO:
        pass
