from fastapi import Request, status

from exceptions.categories import CategoryNotAccessibleError

from presentation.api.app import app
from presentation.api.exception_handlers.common import app_base_exception_to_error


@app.exception_handler(CategoryNotAccessibleError)
async def category_not_accessible_exception_handler(
    request: Request,
    exc: CategoryNotAccessibleError,
):
    return app_base_exception_to_error(
        request=request,
        exc=exc,
        status_code=status.HTTP_404_NOT_FOUND,
    )
