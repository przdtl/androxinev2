from application.dto.templates import (
    GetTodayTemplatesInputDTO,
    GetTodayTemplatesOutputDTO,
)
from application.uow import UnitOfWork


class GetTodayTemplatesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetTodayTemplatesInputDTO,
    ) -> GetTodayTemplatesOutputDTO:
        pass
