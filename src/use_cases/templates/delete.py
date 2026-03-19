from dto.templates import (
    DeleteTemplateInputDTO,
    DeleteTemplateOutputDTO,
)
from exceptions.templates import TemplateAccessDeniedError

from uow import UnitOfWork


class DeleteTemplateUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteTemplateInputDTO,
    ) -> DeleteTemplateOutputDTO:
        template = await self._uow.workout_templates_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            template_id=input_dto.id,
        )
        if template is None:
            raise TemplateAccessDeniedError(
                context={
                    "template_id": str(input_dto.id),
                    "user_id": str(input_dto.user_id),
                }
            )

        await self._uow.workout_templates_dao.delete(template_id=input_dto.id)
        return DeleteTemplateOutputDTO()
