from dto.template_exercises import (
    UpdateTemplateExerciseInputDTO,
    UpdateTemplateExerciseOutputDTO,
)

from uow import UnitOfWork


class UpdateTemplateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateTemplateExerciseInputDTO,
    ) -> UpdateTemplateExerciseOutputDTO:
        return UpdateTemplateExerciseOutputDTO()
