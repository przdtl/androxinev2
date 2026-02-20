from dto.sets import (
    CreateSetInputDTO,
    CreateSetOutputDTO,
)

from uow import UnitOfWork


class CreateSetUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateSetInputDTO,
    ) -> CreateSetOutputDTO:
        return CreateSetOutputDTO()
