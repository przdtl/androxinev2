from typing import Annotated

from fastapi import Depends

from application.uow import UnitOfWork

from infrastructure.uow import InMemoryUnitOfWork


def get_uow() -> UnitOfWork:
    return InMemoryUnitOfWork()


UowDep = Annotated[UnitOfWork, Depends(get_uow)]
