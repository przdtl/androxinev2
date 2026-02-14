from application.dto.categories import (
    ListCategoriesInputDTO,
    ListCategoriesOutputDTO,
)
from application.uow import UnitOfWork


class ListCategoriesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListCategoriesInputDTO,
    ) -> ListCategoriesOutputDTO:
        pass
