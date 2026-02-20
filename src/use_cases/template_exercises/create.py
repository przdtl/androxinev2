from dto.template_exercises import (
    CreateTemplateExerciseInputDTO,
    CreateTemplateExerciseOutputDTO,
)

from uow import UnitOfWork


class CreateTemplateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateTemplateExerciseInputDTO,
    ) -> CreateTemplateExerciseOutputDTO:
        return CreateTemplateExerciseOutputDTO()
