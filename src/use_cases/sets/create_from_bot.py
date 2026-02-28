from dto.sets.create_by_short import (
    CreateSetByExerciseShortInputDTO,
    CreateSetByExerciseShortOutputDTO,
)
from uow import UnitOfWork


class CreateSetFromBotUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        dto: CreateSetByExerciseShortInputDTO,
    ) -> CreateSetByExerciseShortOutputDTO | None:
        exercise = await self._uow.exercises_dao.get_by_user_and_short(
            dto.user_id,
            dto.exercise_short,
        )
        if not exercise:
            return None

        new_set = await self._uow.sets_dao.create(
            user_id=dto.user_id,
            exercise_id=exercise.id,
            weight=dto.weight,
            reps=dto.reps,
            created_at=dto.created_at,
        )

        return CreateSetByExerciseShortOutputDTO(
            id=new_set.id,
            exercise_id=new_set.exercise_id,
            exercise_title=exercise.title,
            weight=new_set.weight,
            reps=new_set.reps,
            created_at=new_set.created_at,
        )
