from application.dto.templates import (
    ListTemplatesInputDTO,
    ListTemplatesOutputDTO,
)
from application.uow import UnitOfWork


class ListTemplatesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListTemplatesInputDTO,
    ) -> ListTemplatesOutputDTO:
        pass
