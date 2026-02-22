from dto.exercises import (
    GetExerciseInputDTO,
    GetExerciseOutputDTO,
)
from dto.exercises.get import CategorySchema

from uow import UnitOfWork


class GetExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetExerciseInputDTO,
    ) -> GetExerciseOutputDTO:
        exercise = await self._uow.exercises_dao.get_by_id(
            exercise_id=input_dto.exercise_id,
        )
        if exercise is None:
            raise ValueError("Exercise not found")

        if exercise.user_id != input_dto.user_id:
            raise ValueError("Exercise does not belong to the user")

        return GetExerciseOutputDTO(
            id=exercise.id,
            title=exercise.title,
            short=exercise.short,
            category=CategorySchema(
                id=exercise.category.id,
                title=exercise.category.title,
            ),
            is_archived=exercise.is_archived,
        )
