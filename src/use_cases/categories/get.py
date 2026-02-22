from dto.categories import (
    GetCategoryInputDTO,
    GetCategoryOutputDTO,
)

from uow import UnitOfWork


class GetCategoryUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetCategoryInputDTO,
    ) -> GetCategoryOutputDTO:
        category = await self._uow.categories_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            category_id=input_dto.category_id,
        )
        if category is None:
            raise ValueError("Category not found or does not belong to the user")

        return GetCategoryOutputDTO(
            id=category.id,
            title=category.title,
        )
