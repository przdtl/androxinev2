from models import Category

from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession


class CategoryDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

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
