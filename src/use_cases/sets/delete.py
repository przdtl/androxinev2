from dto.sets import (
    DeleteSetInputDTO,
    DeleteSetOutputDTO,
)
from exceptions.sets import SetNotAccessibleError

from uow import UnitOfWork


class DeleteSetUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteSetInputDTO,
    ) -> DeleteSetOutputDTO:
        set_item = await self._uow.sets_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            set_id=input_dto.set_id,
        )
        if not set_item:
            raise SetNotAccessibleError()

        await self._uow.sets_dao.delete(set_id=input_dto.set_id)
        return DeleteSetOutputDTO()
