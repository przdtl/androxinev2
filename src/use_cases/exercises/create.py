from dto.exercises import (
    CreateExerciseInputDTO,
    CreateExerciseOutputDTO,
)
from dto.exercises.create import CategorySchema

from uow import UnitOfWork


class CreateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateExerciseInputDTO,
    ) -> CreateExerciseOutputDTO:
        exercise = await self._uow.exercises_dao.create(
            user_id=input_dto.user_id,
            title=input_dto.title,
            short=input_dto.short,
            category_id=input_dto.category_id,
        )
        return CreateExerciseOutputDTO(
            id=exercise.id,
            title=exercise.title,
            short=exercise.short,
            category=CategorySchema(
                id=exercise.category.id,
                title=exercise.category.title,
            ),
            is_archived=exercise.is_archived,
        )
