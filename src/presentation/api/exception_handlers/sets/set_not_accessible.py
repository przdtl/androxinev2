from fastapi import Request, status

from exceptions.sets import SetNotAccessibleError

from presentation.api.app import app
from presentation.api.exception_handlers.common import app_base_exception_to_error


@app.exception_handler(SetNotAccessibleError)
async def set_not_accessible_exception_handler(
    request: Request,
    exc: SetNotAccessibleError,
):
    return app_base_exception_to_error(
        request=request,
        exc=exc,
        status_code=status.HTTP_404_NOT_FOUND,
    )
