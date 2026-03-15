from fastapi import status

from exceptions.common import AppException

from presentation.api.app import app
from presentation.api.schemas.common import APIError, ErrorDetail

from .common import error_response


@app.exception_handler(AppException)
async def app_exception_handler(request, exc: AppException):
    details = [
        ErrorDetail(
            field=str(key),
            code="APP_CONTEXT",
            message=str(value),
        )
        for key, value in exc.context.items()
    ]

    return error_response(
        request=request,
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        data=APIError(
            code=exc.code,
            message=exc.message,
            details=details,
        ),
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return error_response(
        request=request,
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        data=APIError(
            code="INTERNAL_SERVER_ERROR",
            message="Произошла внутренняя ошибка сервера. Пожалуйста, попробуйте позже.",
        ),
    )


@app.exception_handler(status.HTTP_401_UNAUTHORIZED)
async def unauthorized_exception_handler(request, exc):
    return error_response(
        request=request,
        status_code=status.HTTP_401_UNAUTHORIZED,
        data=APIError(
            code="UNAUTHORIZED",
            message="Требуется аутентификация для доступа к этому ресурсу.",
        ),
    )
