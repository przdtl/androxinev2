from application.dto.exercises import (
    ListExercisesInputDTO,
    ListExercisesOutputDTO,
)
from application.dto.exercises.list_excercises import CategorySchema
from application.uow import UnitOfWork


class ListExercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListExercisesInputDTO,
    ) -> list[ListExercisesOutputDTO]:
        exercises = await self._uow.exercises_repo.list()
        return [
            ListExercisesOutputDTO(
                id=exercise.id,
                title=exercise.title,
                short=exercise.short,
                category=CategorySchema(
                    id=exercise.category.id,
                    title=exercise.category.title,
                    created_at=exercise.category.created_at,
                    updated_at=exercise.category.updated_at,
                ),
                created_at=exercise.created_at,
                updated_at=exercise.updated_at,
                is_archived=False,
            )
            for exercise in exercises
        ]
