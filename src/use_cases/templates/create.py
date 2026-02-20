from dto.templates import (
    CreateTemplateInputDTO,
    CreateTemplateOutputDTO,
)

from uow import UnitOfWork


class CreateTemplateUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateTemplateInputDTO,
    ) -> CreateTemplateOutputDTO:
        return CreateTemplateOutputDTO()
