from typing import Annotated

from fastapi import Depends

from application.uow import UnitOfWork


UowDep = Annotated[UnitOfWork, Depends()]
