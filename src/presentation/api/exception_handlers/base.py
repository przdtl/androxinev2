from fastapi import status

from exceptions.account import InvalidTelegramAuthDataError
from exceptions.categories import CategoryNotAccessibleError, CategoryNotFoundError
from exceptions.exercises import (
    ExerciseAccessDeniedError,
    ExerciseNotAccessibleError,
    ExerciseNotFoundError,
)
from exceptions.common import AppException
from exceptions.sets import SetNotAccessibleError, SetNotFoundError
from exceptions.templates import TemplateAccessDeniedError

from presentation.api.app import app
from presentation.api.schemas.common import APIError, ErrorDetail

from .common import error_response


def _status_code_by_exception(exc: AppException) -> int:
    status_map: dict[type[AppException], int] = {
        InvalidTelegramAuthDataError: status.HTTP_401_UNAUTHORIZED,
        CategoryNotFoundError: status.HTTP_404_NOT_FOUND,
        CategoryNotAccessibleError: status.HTTP_404_NOT_FOUND,
        ExerciseNotFoundError: status.HTTP_404_NOT_FOUND,
        ExerciseNotAccessibleError: status.HTTP_404_NOT_FOUND,
        SetNotFoundError: status.HTTP_404_NOT_FOUND,
        SetNotAccessibleError: status.HTTP_404_NOT_FOUND,
        ExerciseAccessDeniedError: status.HTTP_403_FORBIDDEN,
        TemplateAccessDeniedError: status.HTTP_403_FORBIDDEN,
    }
    return status_map.get(type(exc), status.HTTP_400_BAD_REQUEST)


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
        status_code=_status_code_by_exception(exc),
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
