from dto.templates import (
    UpdateTemplateInputDTO,
    UpdateTemplateOutputDTO,
)

from uow import UnitOfWork


class UpdateTemplateUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateTemplateInputDTO,
    ) -> UpdateTemplateOutputDTO:
        return UpdateTemplateOutputDTO()
