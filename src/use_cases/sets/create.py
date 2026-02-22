from dto.sets import (
    CreateSetInputDTO,
    CreateSetOutputDTO,
)
from dto.sets.create import ExerciseSchema, CategorySchema

from uow import UnitOfWork


class CreateSetUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateSetInputDTO,
    ) -> CreateSetOutputDTO:
        exercise = await self._uow.exercises_dao.get_by_id(
            exercise_id=input_dto.exercise_id
        )
        if not exercise:
            raise ValueError("Exercise not found")

        set_item = await self._uow.sets_dao.create(
            user_id=input_dto.user_id,
            exercise_id=input_dto.exercise_id,
            weight=input_dto.weight,
            reps=input_dto.reps,
            created_at=input_dto.created_at,
        )

        return CreateSetOutputDTO(
            id=set_item.id,
            user_id=set_item.user_id,
            exercise=ExerciseSchema(
                id=set_item.exercise.id,
                title=set_item.exercise.title,
                short=set_item.exercise.short,
                category=CategorySchema(
                    id=set_item.exercise.category.id,
                    title=set_item.exercise.category.title,
                ),
                is_archived=set_item.exercise.is_archived,
            ),
            weight=set_item.weight,
            reps=set_item.reps,
            created_at=set_item.created_at,
        )
