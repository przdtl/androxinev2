from application.dto.exercises import (
    ListUserExercisesInputDTO,
    ListUserExercisesOutputDTO,
)
from application.uow import UnitOfWork


class ListUserExercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListUserExercisesInputDTO,
    ) -> list[ListUserExercisesOutputDTO]:
        async with self._uow:
            exercises = await self._uow.exercises_repo.list()
            # Filter by user_id if needed
            return [
                ListUserExercisesOutputDTO(
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
