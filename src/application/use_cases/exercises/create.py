import uuid
import datetime

from application.dto.exercises import (
    CreateExerciseInputDTO,
    CreateExerciseOutputDTO,
)
from application.uow import UnitOfWork
from domain.entities.exercises import Exercise


class CreateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateExerciseInputDTO,
    ) -> CreateExerciseOutputDTO:
        async with self._uow:
            category = await self._uow.categories_repo.get(input_dto.category_id)
            if not category:
                raise ValueError(f"Category {input_dto.category_id} not found")

            now = datetime.datetime.now()
            exercise = Exercise(
                id=uuid.uuid4(),
                title=input_dto.title,
                short=input_dto.short,
                category=category,
                user_id=None,
                created_at=now,
                updated_at=now,
            )

            await self._uow.exercises_repo.add(exercise)
            await self._uow.commit()

            return CreateExerciseOutputDTO(
                id=exercise.id,
                title=exercise.title,
                short=exercise.short,
                category=exercise.category,
                created_at=exercise.created_at,
                updated_at=exercise.updated_at,
                is_archived=False,
            )
