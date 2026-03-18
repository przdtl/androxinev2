from dto.categories import (
    DeleteCategoryInputDTO,
    DeleteCategoryOutputDTO,
)
from exceptions.categories import CategoryNotAccessibleError

from uow import UnitOfWork


class DeleteCategoryUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteCategoryInputDTO,
    ) -> DeleteCategoryOutputDTO:
        category = await self._uow.categories_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            category_id=input_dto.category_id,
        )
        if category is None:
            raise CategoryNotAccessibleError()

        await self._uow.categories_dao.delete(category_id=input_dto.category_id)

        return DeleteCategoryOutputDTO()
