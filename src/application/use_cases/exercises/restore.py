from application.dto.exercises import (
    RestoreExerciseInputDTO,
    RestoreExerciseOutputDTO,
)
from application.uow import UnitOfWork


class RestoreExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: RestoreExerciseInputDTO,
    ) -> RestoreExerciseOutputDTO:
        pass
