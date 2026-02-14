from application.dto.excercises import (
    CreateExcerciseInputDTO,
    CreateExcerciseOutputDTO,
)
from application.uow import UnitOfWork


class CreateExcerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateExcerciseInputDTO,
    ) -> CreateExcerciseOutputDTO:
        pass
