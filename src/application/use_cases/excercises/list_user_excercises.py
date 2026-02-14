from application.dto.excercises import (
    ListUserExcercisesInputDTO,
    ListUserExcercisesOutputDTO,
)
from application.uow import UnitOfWork


class ListUserExercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListUserExcercisesInputDTO,
    ) -> ListUserExcercisesOutputDTO:
        pass
