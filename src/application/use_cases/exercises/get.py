from application.dto.exercises import (
    GetExerciseInputDTO,
    GetExerciseOutputDTO,
)
from application.dto.exercises.get_excercise import CategorySchema
from application.uow import UnitOfWork


class GetExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetExerciseInputDTO,
    ) -> GetExerciseOutputDTO:
        exercise = await self._uow.exercises_repo.get(input_dto.id)
        if not exercise:
            raise ValueError(f"Exercise {input_dto.id} not found")

        return GetExerciseOutputDTO(
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
