import uuid

from abc import ABC, abstractmethod

from domain.entities.templates import WorkoutTemplate


class WorkoutTemplateRepository(ABC):
    @abstractmethod
    async def add(self, template: WorkoutTemplate) -> None: ...

    @abstractmethod
    async def remove(self, template_id: uuid.UUID) -> None: ...

    @abstractmethod
    async def get(self, template_id: uuid.UUID) -> WorkoutTemplate | None: ...

    @abstractmethod
    async def exists(self, template_id: uuid.UUID) -> bool: ...

    @abstractmethod
    async def list(self) -> list[WorkoutTemplate]: ...
