import uuid
import datetime

from dto.categories import (
    ListCategoriesInputDTO,
    ListCategoriesOutputDTO,
)
from uow import UnitOfWork


class ListCategoriesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

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
