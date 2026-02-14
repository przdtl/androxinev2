from application.dto.exercises import (
    ListExercisesInputDTO,
    ListExercisesOutputDTO,
)
from application.uow import UnitOfWork


class ListExercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListExercisesInputDTO,
    ) -> ListExercisesOutputDTO:
        pass
