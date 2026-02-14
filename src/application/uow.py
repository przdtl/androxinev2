from typing import Self

from abc import ABC, abstractmethod

from application.repositories import (
    UserRepository,
    CategoryRepository,
    ExerciseRepository,
    WorkoutTemplateRepository,
)


class UnitOfWork(ABC):
    users_repo: UserRepository
    categories_repo: CategoryRepository
    exercises_repo: ExerciseRepository
    workout_templates_repo: WorkoutTemplateRepository

    @abstractmethod
    async def __aenter__(self) -> Self: ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...

    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def rollback(self) -> None: ...
