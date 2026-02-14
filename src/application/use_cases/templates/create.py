from application.dto.templates import (
    CreateTemplateInputDTO,
    CreateTemplateOutputDTO,
)
from application.uow import UnitOfWork


class CreateTemplateUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateTemplateInputDTO,
    ) -> CreateTemplateOutputDTO:
        pass
