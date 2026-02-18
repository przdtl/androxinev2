from dto.template_exercises import (
    ListTemplateExercisesInputDTO,
    ListTemplateExercisesOutputDTO,
)


class ListTemplateExercisesUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: ListTemplateExercisesInputDTO,
    ) -> list[ListTemplateExercisesOutputDTO]:
        return []
