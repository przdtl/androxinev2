from dto.template_exercises import (
    DeleteTemplateExerciseInputDTO,
    DeleteTemplateExerciseOutputDTO,
)


class DeleteTemplateExerciseUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: DeleteTemplateExerciseInputDTO,
    ) -> DeleteTemplateExerciseOutputDTO:
        return DeleteTemplateExerciseOutputDTO()
