from application.dto.template_excercises import (
    DeleteTemplateExcerciseInputDTO,
    DeleteTemplateExcerciseOutputDTO,
)
from application.uow import UnitOfWork


class DeleteTemplateExcerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteTemplateExcerciseInputDTO,
    ) -> DeleteTemplateExcerciseOutputDTO:
        pass
