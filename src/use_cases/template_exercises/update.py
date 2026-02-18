from dto.template_exercises import (
    UpdateTemplateExerciseInputDTO,
    UpdateTemplateExerciseOutputDTO,
)


class UpdateTemplateExerciseUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: UpdateTemplateExerciseInputDTO,
    ) -> UpdateTemplateExerciseOutputDTO:
        return UpdateTemplateExerciseOutputDTO()
