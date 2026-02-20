import uuid
import datetime

from dto.exercises import (
    ListUserExercisesInputDTO,
    ListUserExercisesOutputDTO,
)
from dto.exercises.list_user_excercises import CategorySchema

from uow import UnitOfWork


class ListUserExercisesUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: ListUserExercisesInputDTO,
    ) -> list[ListUserExercisesOutputDTO]:
        return [
            ListUserExercisesOutputDTO(
                id=uuid.uuid4(),
                title="Exercise 1",
                short="Short description",
                category=CategorySchema(
                    id=uuid.uuid4(),
                    title="Category 1",
                    created_at=datetime.datetime.now(),
                    updated_at=datetime.datetime.now(),
                ),
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
                is_archived=False,
            )
        ]
