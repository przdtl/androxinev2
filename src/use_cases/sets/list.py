from dto.sets import (
    ListSetsInputDTO,
    ListSetsOutputDTO,
)
from dto.sets.list_sets import ExerciseSchema, CategorySchema


class ListSetsUseCase:
    def __init__(self):
        pass

    async def execute(
        self,
        input_dto: ListSetsInputDTO,
    ) -> list[ListSetsOutputDTO]:
        pass
