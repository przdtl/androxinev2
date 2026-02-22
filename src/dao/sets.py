import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from models import Set


class SetsDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, set_id: uuid.UUID) -> Set | None:
        result = await self._session.execute(
            select(Set).where(Set.id == set_id)
        )
        return result.scalar_one_or_none()

    async def get_by_user_and_id(
        self, user_id: int, set_id: uuid.UUID
    ) -> Set | None:
        result = await self._session.execute(
            select(Set).where(Set.user_id == user_id, Set.id == set_id)
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        user_id: int,
        exercise_id: uuid.UUID,
        weight: float,
        reps: int,
    ) -> Set:
        set_item = Set(
            user_id=user_id,
            exercise_id=exercise_id,
            weight=weight,
            reps=reps,
        )
        self._session.add(set_item)
        await self._session.flush()
        return set_item

    async def update(
        self,
        set_id: uuid.UUID,
        weight: float | None = None,
        reps: int | None = None,
    ) -> Set:
        set_item = await self.get_by_id(set_id)
        if not set_item:
            raise ValueError(f"Set {set_id} not found")

        if weight is not None:
            set_item.weight = weight
        if reps is not None:
            set_item.reps = reps

        await self._session.flush()
        return set_item

    async def delete(self, set_id: uuid.UUID) -> None:
        set_item = await self.get_by_id(set_id)
        if not set_item:
            raise ValueError(f"Set {set_id} not found")

        await self._session.delete(set_item)
        await self._session.flush()

    async def list_by_user_id(
        self,
        user_id: int,
        page: int,
        size: int,
    ) -> list[Set]:
        offset = (page - 1) * size
        result = await self._session.execute(
            select(Set)
            .where(Set.user_id == user_id)
            .order_by(Set.created_at.desc())
            .offset(offset)
            .limit(size)
        )
        return result.scalars().all()

    async def list_by_exercise_id(
        self,
        exercise_id: uuid.UUID,
        page: int,
        size: int,
    ) -> list[Set]:
        offset = (page - 1) * size
        result = await self._session.execute(
            select(Set)
            .where(Set.exercise_id == exercise_id)
            .order_by(Set.created_at.desc())
            .offset(offset)
            .limit(size)
        )
        return result.scalars().all()

    async def count_by_user_id(self, user_id: int) -> int:
        result = await self._session.execute(
            select(Set).where(Set.user_id == user_id)
        )
        return len(result.scalars().all())
