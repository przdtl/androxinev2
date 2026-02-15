from application.dto.templates import (
    DeleteTemplateInputDTO,
    DeleteTemplateOutputDTO,
)
from application.uow import UnitOfWork


class DeleteTemplateUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteTemplateInputDTO,
    ) -> DeleteTemplateOutputDTO:
        async with self._uow:
            template = await self._uow.workout_templates_repo.get(input_dto.id)
            if not template:
                raise ValueError(f"Template {input_dto.id} not found")

            await self._uow.workout_templates_repo.remove(input_dto.id)
            await self._uow.commit()

            return DeleteTemplateOutputDTO()
