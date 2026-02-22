from dto.sets import (
    UpdateSetInputDTO,
    UpdateSetOutputDTO,
)
from dto.sets.update import ExerciseSchema, CategorySchema

from uow import UnitOfWork


class UpdateSetUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: UpdateSetInputDTO,
    ) -> UpdateSetOutputDTO:
        set_item = await self._uow.sets_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            set_id=input_dto.set_id,
        )
        if not set_item:
            raise ValueError("Set not found or does not belong to the user")

        updated_set = await self._uow.sets_dao.update(
            set_id=input_dto.set_id,
            weight=input_dto.weight,
            reps=input_dto.reps,
        )

        return UpdateSetOutputDTO(
            id=updated_set.id,
            user_id=updated_set.user_id,
            exercise=ExerciseSchema(
                id=updated_set.exercise.id,
                title=updated_set.exercise.title,
                short=updated_set.exercise.short,
                category=CategorySchema(
                    id=updated_set.exercise.category.id,
                    title=updated_set.exercise.category.title,
                ),
                is_archived=updated_set.exercise.is_archived,
            ),
            weight=updated_set.weight,
            reps=updated_set.reps,
        )
