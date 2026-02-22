from dto.categories import (
    DeleteCategoryInputDTO,
    DeleteCategoryOutputDTO,
)

from uow import UnitOfWork


class DeleteCategoryUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteCategoryInputDTO,
    ) -> DeleteCategoryOutputDTO:
        # Проверяем, что категория принадлежит пользователю
        category = await self._uow.categories_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            category_id=input_dto.category_id,
        )
        if category is None:
            raise ValueError("Category not found or does not belong to the user")

        # Удаляем категорию
        await self._uow.categories_dao.delete(category_id=input_dto.category_id)

        return DeleteCategoryOutputDTO()
