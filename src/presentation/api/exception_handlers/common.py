from fastapi import Request
from fastapi.responses import JSONResponse

from presentation.api.schemas.common import APIError, ErrorResponse


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
