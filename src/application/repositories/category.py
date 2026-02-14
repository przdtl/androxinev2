import uuid

from abc import ABC, abstractmethod

from domain.entities.exercises import Category


class CategoryRepository(ABC):
    @abstractmethod
    async def add(self, category: Category) -> None: ...

    @abstractmethod
    async def remove(self, category_id: uuid.UUID) -> None: ...

    @abstractmethod
    async def get(self, category_id: uuid.UUID) -> Category | None: ...

    @abstractmethod
    async def exists(self, category_id: uuid.UUID) -> bool: ...

    @abstractmethod
    async def list(self) -> list[Category]: ...
