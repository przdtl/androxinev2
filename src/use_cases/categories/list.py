import uuid
import datetime

from dto.categories import (
    ListCategoriesInputDTO,
    ListCategoriesOutputDTO,
)


class ListCategoriesUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: ListCategoriesInputDTO,
    ) -> list[ListCategoriesOutputDTO]:
        return [
            ListCategoriesOutputDTO(
                id=uuid.uuid4(),
                title="Category 1",
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            )
        ]
