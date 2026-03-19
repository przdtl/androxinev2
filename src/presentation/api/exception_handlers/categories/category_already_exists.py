from fastapi import Request, status

from exceptions.categories import CategoryAlreadyExistsError

from presentation.api.app import app
from presentation.api.exception_handlers.common import app_base_exception_to_error


@app.exception_handler(CategoryAlreadyExistsError)
async def category_already_exists_exception_handler(
    request: Request,
    exc: CategoryAlreadyExistsError,
):
    return app_base_exception_to_error(
        request=request,
        exc=exc,
        status_code=status.HTTP_409_CONFLICT,
    )
