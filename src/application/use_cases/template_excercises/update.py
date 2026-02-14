from application.dto.template_excercises import (
    UpdateTemplateExcerciseInputDTO,
    UpdateTemplateExcerciseOutputDTO,
)
from application.uow import UnitOfWork


class UpdateTemplateExcerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateTemplateExcerciseInputDTO,
    ) -> UpdateTemplateExcerciseOutputDTO:
        pass
