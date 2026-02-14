from application.dto.templates import (
    DeleteTemplateInputDTO,
    DeleteTemplateOutputDTO,
)
from application.uow import UnitOfWork


class DeleteTemplateUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteTemplateInputDTO,
    ) -> DeleteTemplateOutputDTO:
        pass
