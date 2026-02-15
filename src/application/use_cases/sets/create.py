import uuid
import datetime

from application.dto.sets import (
    CreateSetInputDTO,
    CreateSetOutputDTO,
)
from application.uow import UnitOfWork
from domain.entities.sets import Set


class CreateSetUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: CreateSetInputDTO,
    ) -> CreateSetOutputDTO:
        exercise = await self._uow.exercises_repo.get(input_dto.exercise_id)
        if not exercise:
            raise ValueError(f"Exercise {input_dto.exercise_id} not found")

        set_entity = Set(
            id=uuid.uuid4(),
            user_id=1,  # TODO: get from context
            exercise_id=input_dto.exercise_id,
            weight=input_dto.weight,
            reps=input_dto.reps,
            created_at=datetime.datetime.now(),
        )

        await self._uow.sets_repo.add(set_entity)
        await self._uow.commit()

        return CreateSetOutputDTO(
            id=set_entity.id,
            user_id=set_entity.user_id,
            exercise=exercise,
            weight=set_entity.weight,
            reps=set_entity.reps,
            created_at=set_entity.created_at,
        )
