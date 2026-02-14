from application.dto.excercises import (
    ListExcercisesInputDTO,
    ListExcercisesOutputDTO,
)
from application.uow import UnitOfWork


class ListExcercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListExcercisesInputDTO,
    ) -> ListExcercisesOutputDTO:
        pass
