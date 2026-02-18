import datetime

from dto.templates import (
    GetTodayTemplatesInputDTO,
    GetTodayTemplatesOutputDTO,
)


class GetTodayTemplatesUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: GetTodayTemplatesInputDTO,
    ) -> list[GetTodayTemplatesOutputDTO]:
        return []
