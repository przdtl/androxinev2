from application.dto.template_excercises import (
    ListTemplateExcercisesInputDTO,
    ListTemplateExcercisesOutputDTO,
)
from application.uow import UnitOfWork


class ListTemplateExcercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListTemplateExcercisesInputDTO,
    ) -> ListTemplateExcercisesOutputDTO:
        pass
