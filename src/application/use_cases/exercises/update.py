from application.dto.exercises import (
    UpdateExerciseInputDTO,
    UpdateExerciseOutputDTO,
)
from application.uow import UnitOfWork


class UpdateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateExerciseInputDTO,
    ) -> UpdateExerciseOutputDTO:
        pass
