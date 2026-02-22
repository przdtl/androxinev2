from dto.categories import (
    UpdateCategoryInputDTO,
    UpdateCategoryOutputDTO,
)

from uow import UnitOfWork


class UpdateCategoryUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateCategoryInputDTO,
    ) -> UpdateCategoryOutputDTO:
        # Проверяем, что категория принадлежит пользователю
        category = await self._uow.categories_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            category_id=input_dto.category_id,
        )
        if category is None:
            raise ValueError("Category not found or does not belong to the user")

        # Обновляем категорию
        updated_category = await self._uow.categories_dao.update(
            category_id=input_dto.category_id,
            title=input_dto.title,
        )

        return UpdateCategoryOutputDTO(
            id=updated_category.id,
            title=updated_category.title,
        )
