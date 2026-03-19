from fastapi import Request, status

from exceptions.account import InvalidTelegramAuthDataError

from presentation.api.app import app
from presentation.api.exception_handlers.common import app_base_exception_to_error


@app.exception_handler(InvalidTelegramAuthDataError)
async def invalid_telegram_auth_data_exception_handler(
    request: Request, exc: InvalidTelegramAuthDataError
):
    return app_base_exception_to_error(
        request=request,
        exc=exc,
        status_code=status.HTTP_400_BAD_REQUEST,
    )
