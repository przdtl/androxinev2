from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_session

from uow import UnitOfWork


async def get_uow(
    session: AsyncSession = Depends(get_session),
):
    async with UnitOfWork(session) as uow:
        yield uow


UOWDep = Annotated[UnitOfWork, Depends(get_uow)]
