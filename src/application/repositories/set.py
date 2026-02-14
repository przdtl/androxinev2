import uuid

from abc import ABC, abstractmethod

from domain.entities.sets import Set


class SetRepository(ABC):
    @abstractmethod
    async def add(self, set_entity: Set) -> None: ...

    @abstractmethod
    async def remove(self, set_id: uuid.UUID) -> None: ...

    @abstractmethod
    async def get(self, set_id: uuid.UUID) -> Set | None: ...

    @abstractmethod
    async def exists(self, set_id: uuid.UUID) -> bool: ...

    @abstractmethod
    async def list(self) -> list[Set]: ...
