from application.dto.template_exercises import (
    DeleteTemplateExerciseInputDTO,
    DeleteTemplateExerciseOutputDTO,
)
from application.uow import UnitOfWork


class DeleteTemplateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteTemplateExerciseInputDTO,
    ) -> DeleteTemplateExerciseOutputDTO:
        async with self._uow:
            # In real implementation, find and delete template exercise from template
            await self._uow.commit()
            return DeleteTemplateExerciseOutputDTO()
