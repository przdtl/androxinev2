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
        categories = await self._uow.categories_dao.list_by_user_id(
            user_id=input_dto.user_id,
            page=input_dto.page,
            size=input_dto.size,
        )

        return [
            ListCategoriesOutputDTO(
                id=category.id,
                title=category.title,
            )
            for category in categories
        ]
