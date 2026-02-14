from application.dto.template_exercises import (
    UpdateTemplateExerciseInputDTO,
    UpdateTemplateExerciseOutputDTO,
)
from application.uow import UnitOfWork


class UpdateTemplateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateTemplateExerciseInputDTO,
    ) -> UpdateTemplateExerciseOutputDTO:
        pass
