from fastapi import Request, status

from exceptions.account import UserNotFoundError

from presentation.api.app import app
from presentation.api.exception_handlers.common import app_base_exception_to_error


@app.exception_handler(UserNotFoundError)
async def user_not_found_exception_handler(
    request: Request,
    exc: UserNotFoundError,
):
    return app_base_exception_to_error(
        request=request,
        exc=exc,
        status_code=status.HTTP_404_NOT_FOUND,
    )
