from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncAttrs,
    create_async_engine,
    async_sessionmaker,
)

from infrastructure.config import settings

engine = create_async_engine(
    settings.DB_URL,
    echo=True,
)

async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


class Base(AsyncAttrs, DeclarativeBase):
    pass
