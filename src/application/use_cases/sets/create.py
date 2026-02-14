from application.dto.sets import (
    CreateSetInputDTO,
    CreateSetOutputDTO,
)
from application.uow import UnitOfWork


class CreateSetUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateSetInputDTO,
    ) -> CreateSetOutputDTO:
        pass
