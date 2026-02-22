from dto.sets import (
    ListSetsInputDTO,
    ListSetsOutputDTO,
)
from dto.sets.list import ExerciseSchema, CategorySchema

from uow import UnitOfWork


class ListSetsUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListSetsInputDTO,
    ) -> list[ListSetsOutputDTO]:
        sets = await self._uow.sets_dao.list_by_user_id(
            user_id=input_dto.user_id,
            page=input_dto.page,
            size=input_dto.size,
            exercise_id=input_dto.exercise_id,
            created_from=input_dto.created_from,
            created_to=input_dto.created_to,
        )

        return [
            ListSetsOutputDTO(
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
            for set_item in sets
        ]
