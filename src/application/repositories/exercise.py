import uuid

from abc import ABC, abstractmethod

from domain.entities.excercises import Exercise


class ExerciseRepository(ABC):
    @abstractmethod
    async def add(self, exercise: Exercise) -> None: ...

    @abstractmethod
    async def remove(self, exercise_id: uuid.UUID) -> None: ...

    @abstractmethod
    async def get(self, exercise_id: uuid.UUID) -> Exercise | None: ...

    @abstractmethod
    async def exists(self, exercise_id: uuid.UUID) -> bool: ...

    @abstractmethod
    async def list(self) -> list[Exercise]: ...
