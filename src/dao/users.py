from sqlalchemy.ext.asyncio.session import AsyncSession

from models.users import User


class UsersDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(
        self,
        telegram_id: int,
        first_name: str,
        last_name: str | None = None,
        username: str | None = None,
        photo_url: str | None = None,
    ) -> User:
        new_user = User(
            id=telegram_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            photo_url=photo_url,
        )
        self._session.add(new_user)
        return new_user

    async def get_by_id(self, telegram_id: int) -> User | None:
        user = await self._session.execute(
            User.__table__.select().where(User.id == telegram_id)
        )
        return user.scalar_one_or_none()

    async def update(
        self,
        telegram_id: int,
        first_name: str | None = None,
        last_name: str | None = None,
        username: str | None = None,
        photo_url: str | None = None,
    ) -> User:
        user = await self.get_by_id(telegram_id)
        if not user:
            raise ValueError("User not found")

        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if username is not None:
            user.username = username
        if photo_url is not None:
            user.photo_url = photo_url

        return user
