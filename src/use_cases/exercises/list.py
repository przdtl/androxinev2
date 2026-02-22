from dto.exercises import (
    ListExercisesInputDTO,
    ListExercisesOutputDTO,
)
from dto.exercises.list_excercises import CategorySchema

from uow import UnitOfWork


class ListExercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListExercisesInputDTO,
    ) -> list[ListExercisesOutputDTO]:
        exercises = await self._uow.exercises_dao.list_by_user_id(
            user_id=input_dto.user_id,
            page=input_dto.page,
            size=input_dto.size,
        )

        return [
            ListExercisesOutputDTO(
                id=exercise.id,
                title=exercise.title,
                short=exercise.short,
                category=CategorySchema(
                    id=exercise.category.id,
                    title=exercise.category.title,
                ),
                is_archived=exercise.is_archived,
            )
            for exercise in exercises
        ]
