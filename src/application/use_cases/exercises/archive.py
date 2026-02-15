from application.dto.exercises import (
    ArchiveExerciseInputDTO,
    ArchiveExerciseOutputDTO,
)
from application.uow import UnitOfWork


# TODO: implement archiving logic (is_archived flag)
class ArchiveExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ArchiveExerciseInputDTO,
    ) -> ArchiveExerciseOutputDTO:
        exercise = await self._uow.exercises_repo.get(input_dto.id)
        if not exercise:
            raise ValueError(f"Exercise {input_dto.id} not found")

        # In real implementation, update is_archived flag
        await self._uow.commit()

        return ArchiveExerciseOutputDTO(
            id=exercise.id,
            title=exercise.title,
            short=exercise.short,
            category=exercise.category,
            created_at=exercise.created_at,
            updated_at=exercise.updated_at,
            is_archived=True,
        )
