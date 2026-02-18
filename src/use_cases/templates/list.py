from dto.templates import (
    ListTemplatesInputDTO,
    ListTemplatesOutputDTO,
)


class ListTemplatesUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: ListTemplatesInputDTO,
    ) -> list[ListTemplatesOutputDTO]:
        return []
