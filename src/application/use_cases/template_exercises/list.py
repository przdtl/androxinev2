from application.dto.template_exercises import (
    ListTemplateExercisesInputDTO,
    ListTemplateExercisesOutputDTO,
)
from application.uow import UnitOfWork


class ListTemplateExercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListTemplateExercisesInputDTO,
    ) -> list[ListTemplateExercisesOutputDTO]:
        async with self._uow:
            # In real implementation, query template exercises
            # For now, return empty list
            return []
