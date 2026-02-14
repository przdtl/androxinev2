from application.dto.exercises import (
    CreateExerciseInputDTO,
    CreateExerciseOutputDTO,
)
from application.uow import UnitOfWork


class CreateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateExerciseInputDTO,
    ) -> CreateExerciseOutputDTO:
        pass
