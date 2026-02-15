from application.dto.exercises import (
    GetExerciseInputDTO,
    GetExerciseOutputDTO,
)
from application.uow import UnitOfWork


class GetExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetExerciseInputDTO,
    ) -> GetExerciseOutputDTO:
        async with self._uow:
            exercise = await self._uow.exercises_repo.get(input_dto.id)
            if not exercise:
                raise ValueError(f"Exercise {input_dto.id} not found")

            return GetExerciseOutputDTO(
                id=exercise.id,
                title=exercise.title,
                short=exercise.short,
                category=exercise.category,
                created_at=exercise.created_at,
                updated_at=exercise.updated_at,
                is_archived=False,
            )
