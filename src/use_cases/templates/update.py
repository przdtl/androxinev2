import datetime

from dto.templates import (
    UpdateTemplateInputDTO,
    UpdateTemplateOutputDTO,
)


class UpdateTemplateUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: UpdateTemplateInputDTO,
    ) -> UpdateTemplateOutputDTO:
        return UpdateTemplateOutputDTO()
