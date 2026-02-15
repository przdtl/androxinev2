import uuid
import datetime

from domain.entities.exercises import Exercise

from application.dto.exercises import (
    CreateExerciseInputDTO,
    CreateExerciseOutputDTO,
)
from application.dto.exercises.create_excercise import CategorySchema
from application.uow import UnitOfWork


class CreateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateExerciseInputDTO,
    ) -> CreateExerciseOutputDTO:
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
