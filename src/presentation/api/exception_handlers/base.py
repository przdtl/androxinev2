from presentation.api.app import app
from presentation.api.schemas.common import APIError

from .common import error_response


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return error_response(
        request=request,
        status_code=500,
        data=APIError(
            code="INTERNAL_SERVER_ERROR",
            message="Произошла внутренняя ошибка сервера. Пожалуйста, попробуйте позже.",
        ),
    )
