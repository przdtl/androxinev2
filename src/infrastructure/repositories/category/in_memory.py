import uuid

from domain.entities.exercises import Category

from application.repositories.category import CategoryRepository

storage: dict[uuid.UUID, Category] = {}


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self):
        self._storage: dict[uuid.UUID, Category] = storage

    async def add(self, category: Category) -> None:
        self._storage[category.id] = category

    async def remove(self, category_id: uuid.UUID) -> None:
        if category_id in self._storage:
            del self._storage[category_id]

    async def get(self, category_id: uuid.UUID) -> Category | None:
        return self._storage.get(category_id)

    async def exists(self, category_id: uuid.UUID) -> bool:
        return category_id in self._storage

    async def list(self) -> list[Category]:
        return list(self._storage.values())
