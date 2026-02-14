from application.dto.template_excercises import (
    CreateTemplateExcerciseInputDTO,
    CreateTemplateExcerciseOutputDTO,
)
from application.uow import UnitOfWork


class CreateTemplateExcerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateTemplateExcerciseInputDTO,
    ) -> CreateTemplateExcerciseOutputDTO:
        pass
