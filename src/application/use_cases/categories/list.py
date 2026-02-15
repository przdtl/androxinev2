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
    ) -> list[ListCategoriesOutputDTO]:
        async with self._uow:
            categories = await self._uow.categories_repo.list()
            return [
                ListCategoriesOutputDTO(
                    id=category.id,
                    title=category.title,
                    created_at=category.created_at,
                    updated_at=category.updated_at,
                )
                for category in categories
            ]
