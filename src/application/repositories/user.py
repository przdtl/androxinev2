from abc import ABC, abstractmethod

from domain.entities.users import User


class UserRepository(ABC):
    @abstractmethod
    async def add(self, user: User) -> None: ...

    @abstractmethod
    async def remove(self, user_id: int) -> None: ...

    @abstractmethod
    async def get(self, user_id: int) -> User | None: ...

    @abstractmethod
    async def exists(self, user_id: int) -> bool: ...

    @abstractmethod
    async def list(self) -> list[User]: ...
