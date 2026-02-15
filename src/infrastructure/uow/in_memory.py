from typing import Self

from application.uow import UnitOfWork
from infrastructure.repositories.category import InMemoryCategoryRepository
from infrastructure.repositories.exercise import InMemoryExerciseRepository
from infrastructure.repositories.set import InMemorySetRepository
from infrastructure.repositories.user import InMemoryUserRepository
from infrastructure.repositories.workout_template import (
    InMemoryWorkoutTemplateRepository,
)


class InMemoryUnitOfWork(UnitOfWork):
    def __init__(self):
        self.users_repo = InMemoryUserRepository()
        self.categories_repo = InMemoryCategoryRepository()
        self.exercises_repo = InMemoryExerciseRepository()
        self.workout_templates_repo = InMemoryWorkoutTemplateRepository()
        self.sets_repo = InMemorySetRepository()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self) -> None:
        # In-memory implementation doesn't need explicit commit
        pass

    async def rollback(self) -> None:
        # In-memory implementation doesn't support rollback
        # In a real scenario, you might want to implement transaction snapshots
        pass
