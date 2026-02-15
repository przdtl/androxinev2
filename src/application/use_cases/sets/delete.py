from application.dto.sets import (
    DeleteSetInputDTO,
    DeleteSetOutputDTO,
)
from application.uow import UnitOfWork


class DeleteSetUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteSetInputDTO,
    ) -> DeleteSetOutputDTO:
        set_entity = await self._uow.sets_repo.get(input_dto.id)
        if not set_entity:
            raise ValueError(f"Set {input_dto.id} not found")

        await self._uow.sets_repo.remove(input_dto.id)
        await self._uow.commit()

        return DeleteSetOutputDTO()
