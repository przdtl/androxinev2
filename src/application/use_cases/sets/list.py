from application.dto.sets import (
    ListSetsInputDTO,
    ListSetsOutputDTO,
)
from application.uow import UnitOfWork


class ListSetsUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListSetsInputDTO,
    ) -> list[ListSetsOutputDTO]:
        async with self._uow:
            sets = await self._uow.sets_repo.list()
            result = []
            for set_entity in sets:
                exercise = await self._uow.exercises_repo.get(set_entity.exercise_id)
                if exercise:
                    result.append(
                        ListSetsOutputDTO(
                            id=set_entity.id,
                            user_id=set_entity.user_id,
                            exercise=exercise,
                            weight=set_entity.weight,
                            reps=set_entity.reps,
                            created_at=set_entity.created_at,
                        )
                    )
            return result
