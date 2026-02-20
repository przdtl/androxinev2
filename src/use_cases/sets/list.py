from dto.sets import (
    ListSetsInputDTO,
    ListSetsOutputDTO,
)

from uow import UnitOfWork


class ListSetsUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListSetsInputDTO,
    ) -> list[ListSetsOutputDTO]:
        pass
