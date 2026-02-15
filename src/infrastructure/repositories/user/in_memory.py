from domain.entities.users import User

from application.repositories.user import UserRepository

storage: dict[int, User] = {}


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._storage: dict[int, User] = storage

    async def add(self, user: User) -> None:
        self._storage[user.id] = user

    async def remove(self, user_id: int) -> None:
        if user_id in self._storage:
            del self._storage[user_id]

    async def get(self, user_id: int) -> User | None:
        return self._storage.get(user_id)

    async def exists(self, user_id: int) -> bool:
        return user_id in self._storage

    async def list(self) -> list[User]:
        return list(self._storage.values())
