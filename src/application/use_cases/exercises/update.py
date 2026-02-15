import datetime

from application.dto.exercises import (
    UpdateExerciseInputDTO,
    UpdateExerciseOutputDTO,
)
from application.uow import UnitOfWork


class UpdateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateExerciseInputDTO,
    ) -> UpdateExerciseOutputDTO:
        exercise = await self._uow.exercises_repo.get(input_dto.id)
        if not exercise:
            raise ValueError(f"Exercise {input_dto.id} not found")

        if input_dto.title is not None:
            exercise.update_title(input_dto.title)
        if input_dto.short is not None:
            exercise.update_short(input_dto.short)

        await self._uow.commit()

        return UpdateExerciseOutputDTO(
            id=exercise.id,
            title=exercise.title,
            short=exercise.short,
            category=exercise.category,
            created_at=exercise.created_at,
            updated_at=datetime.datetime.now(),
            is_archived=False,
        )
