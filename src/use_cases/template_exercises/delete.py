from dto.template_exercises import (
    DeleteTemplateExerciseInputDTO,
    DeleteTemplateExerciseOutputDTO,
)

from uow import UnitOfWork


class DeleteTemplateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteTemplateExerciseInputDTO,
    ) -> DeleteTemplateExerciseOutputDTO:
        return DeleteTemplateExerciseOutputDTO()
