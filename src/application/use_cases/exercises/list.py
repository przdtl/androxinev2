from application.dto.exercises import (
    ListExercisesInputDTO,
    ListExercisesOutputDTO,
)
from application.uow import UnitOfWork


class ListExercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListExercisesInputDTO,
    ) -> list[ListExercisesOutputDTO]:
        async with self._uow:
            exercises = await self._uow.exercises_repo.list()
            return [
                ListExercisesOutputDTO(
                    id=exercise.id,
                    title=exercise.title,
                    short=exercise.short,
                    category=exercise.category,
                    created_at=exercise.created_at,
                    updated_at=exercise.updated_at,
                    is_archived=False,
                )
                for exercise in exercises
            ]
