from fastapi import Request, status

from exceptions.sets import SetNotFoundError

from presentation.api.app import app
from presentation.api.exception_handlers.common import app_base_exception_to_error


@app.exception_handler(SetNotFoundError)
async def set_not_found_exception_handler(
    request: Request,
    exc: SetNotFoundError,
):
    return app_base_exception_to_error(
        request=request,
        exc=exc,
        status_code=status.HTTP_404_NOT_FOUND,
    )
