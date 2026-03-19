from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions import AppException

from presentation.api.schemas.common import APIError, ErrorResponse, ErrorDetail


def request_id_from(request: Request) -> str | None:
    return getattr(request.state, "request_id", None)


def error_response(
    request: Request,
    status_code: int,
    data: APIError,
) -> JSONResponse:
    data.code = data.code.upper()
    data.request_id = request_id_from(request)
    payload = ErrorResponse(error=data)

    return JSONResponse(status_code=status_code, content=payload.model_dump())


def app_base_exception_to_error(
    request: Request,
    exc: AppException,
    status_code: int,
) -> JSONResponse:
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
        status_code=status_code,
        data=APIError(
            code=exc.CODE,
            message=exc.MESSAGE,
            details=details,
        ),
    )
