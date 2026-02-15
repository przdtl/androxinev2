import uuid

from domain.entities.sets import Set

from application.repositories.set import SetRepository

storage: dict[uuid.UUID, Set] = {}


class InMemorySetRepository(SetRepository):
    def __init__(self):
        self._storage: dict[uuid.UUID, Set] = storage

    async def add(self, set_entity: Set) -> None:
        self._storage[set_entity.id] = set_entity

    async def remove(self, set_id: uuid.UUID) -> None:
        if set_id in self._storage:
            del self._storage[set_id]

    async def get(self, set_id: uuid.UUID) -> Set | None:
        return self._storage.get(set_id)

    async def exists(self, set_id: uuid.UUID) -> bool:
        return set_id in self._storage

    async def list(self) -> list[Set]:
        return list(self._storage.values())
