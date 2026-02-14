from application.dto.exercises import (
    GetExerciseInputDTO,
    GetExerciseOutputDTO,
)
from application.uow import UnitOfWork


class GetExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetExerciseInputDTO,
    ) -> GetExerciseOutputDTO:
        pass
