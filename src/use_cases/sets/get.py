from dto.sets import (
    GetSetInputDTO,
    GetSetOutputDTO,
)
from dto.sets.get import ExerciseSchema, CategorySchema

from uow import UnitOfWork


class GetSetUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: GetSetInputDTO,
    ) -> GetSetOutputDTO:
        set_item = await self._uow.sets_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            set_id=input_dto.set_id,
        )
        if not set_item:
            raise ValueError("Set not found or does not belong to the user")

        return GetSetOutputDTO(
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
        )
