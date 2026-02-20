from dto.templates import (
    ListTemplatesInputDTO,
    ListTemplatesOutputDTO,
)

from uow import UnitOfWork


class ListTemplatesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListTemplatesInputDTO,
    ) -> list[ListTemplatesOutputDTO]:
        return []
