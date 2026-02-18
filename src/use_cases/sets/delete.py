from dto.sets import (
    DeleteSetInputDTO,
    DeleteSetOutputDTO,
)


class DeleteSetUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: DeleteSetInputDTO,
    ) -> DeleteSetOutputDTO:
        return DeleteSetOutputDTO()
