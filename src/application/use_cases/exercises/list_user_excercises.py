from application.dto.exercises import (
    ListUserExercisesInputDTO,
    ListUserExercisesOutputDTO,
)
from application.uow import UnitOfWork


class ListUserExercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListUserExercisesInputDTO,
    ) -> list[ListUserExercisesOutputDTO]:
        pass
