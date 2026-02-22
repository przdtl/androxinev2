from dto.exercises import (
    DeleteExerciseInputDTO,
    DeleteExerciseOutputDTO,
)

from uow import UnitOfWork


class DeleteExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteExerciseInputDTO,
    ) -> DeleteExerciseOutputDTO:
        # Проверяем, что упражнение принадлежит пользователю
        exercise = await self._uow.exercises_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            exercise_id=input_dto.exercise_id,
        )
        if exercise is None:
            raise ValueError("Exercise not found or does not belong to the user")

        # Удаляем упражнение
        await self._uow.exercises_dao.delete(exercise_id=input_dto.exercise_id)

        return DeleteExerciseOutputDTO()
