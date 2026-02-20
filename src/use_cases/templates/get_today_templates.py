from dto.templates import (
    GetTodayTemplatesInputDTO,
    GetTodayTemplatesOutputDTO,
)

from uow import UnitOfWork


class GetTodayTemplatesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetTodayTemplatesInputDTO,
    ) -> list[GetTodayTemplatesOutputDTO]:
        return []
