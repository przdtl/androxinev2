from dto.categories import (
    CreateCategoryInputDTO,
    CreateCategoryOutputDTO,
)

from uow import UnitOfWork


class CreateCategoryUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateCategoryInputDTO,
    ) -> CreateCategoryOutputDTO:
        category = await self._uow.categories_dao.create(
            user_id=input_dto.user_id,
            title=input_dto.title,
        )
        return CreateCategoryOutputDTO(
            id=category.id,
            title=category.title,
        )
