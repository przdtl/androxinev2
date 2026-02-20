from dto.sets import (
    DeleteSetInputDTO,
    DeleteSetOutputDTO,
)

from uow import UnitOfWork


class DeleteSetUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteSetInputDTO,
    ) -> DeleteSetOutputDTO:
        return DeleteSetOutputDTO()
