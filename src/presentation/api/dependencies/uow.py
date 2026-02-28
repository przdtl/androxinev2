from typing import Annotated

from fastapi import Depends

from uow import UnitOfWork

from presentation.api.dependencies.db import SessionDep


async def get_uow(
    session: SessionDep,
):
    async with UnitOfWork(session) as uow:
        yield uow


UOWDep = Annotated[UnitOfWork, Depends(get_uow)]
