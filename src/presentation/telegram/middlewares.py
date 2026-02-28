from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from db.base import async_session_maker
from uow import UnitOfWork


class UOWMiddleware(BaseMiddleware):
    """
    Middleware для автоматической инъекции UnitOfWork в контекст.

    Использование в handler:
    ```python
    async def my_handler(message: Message, uow: UnitOfWork):
        # uow доступен напрямую как параметр
        async with uow:
            use_case = SomeUseCase(uow)
            result = await use_case.execute(dto)
    ```
    """

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        async with async_session_maker() as session:
            async with UnitOfWork(session) as uow:
                data["uow"] = uow
                return await handler(event, data)
