from dto.template_exercises import (
    ListTemplateExercisesInputDTO,
    ListTemplateExercisesOutputDTO,
)

from uow import UnitOfWork


class ListTemplateExercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListTemplateExercisesInputDTO,
    ) -> list[ListTemplateExercisesOutputDTO]:
        return []
