import uuid

from models import Category

from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession


class CategoryDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, category_id: uuid.UUID) -> Category | None:
        result = await self._session.execute(
            select(Category).where(Category.id == category_id)
        )
        return result.scalar_one_or_none()

    async def get_by_user_and_id(
        self, user_id: int, category_id: uuid.UUID
    ) -> Category | None:
        result = await self._session.execute(
            select(Category).where(
                Category.user_id == user_id, Category.id == category_id
            )
        )
        return result.scalar_one_or_none()

    async def create(self, user_id: int, title: str) -> Category:
        category = Category(user_id=user_id, title=title)
        self._session.add(category)
        await self._session.flush()
        return category

    async def update(self, category_id: uuid.UUID, title: str) -> Category:
        category = await self.get_by_id(category_id)
        if not category:
            raise ValueError(f"Category {category_id} not found")

        category.title = title
        await self._session.flush()
        return category

    async def delete(self, category_id: uuid.UUID) -> None:
        category = await self.get_by_id(category_id)
        if not category:
            raise ValueError(f"Category {category_id} not found")

        await self._session.delete(category)
        await self._session.flush()

    async def create_default_for_user(self, user_id: int) -> list[Category]:
        default_categories = [
            Category(user_id=user_id, title="Грудь"),
            Category(user_id=user_id, title="Спина"),
            Category(user_id=user_id, title="Ноги"),
        ]

        self._session.add_all(default_categories)
        await self._session.flush()

        return default_categories

    async def list_by_user_id(
        self, user_id: int, page: int, size: int
    ) -> list[Category]:
        offset = (page - 1) * size

        result = await self._session.execute(
            select(Category)
            .where(Category.user_id == user_id)
            .offset(offset)
            .limit(size)
        )

        return result.scalars().all()
