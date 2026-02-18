from dto.templates import (
    DeleteTemplateInputDTO,
    DeleteTemplateOutputDTO,
)


class DeleteTemplateUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: DeleteTemplateInputDTO,
    ) -> DeleteTemplateOutputDTO:
        return DeleteTemplateOutputDTO()
