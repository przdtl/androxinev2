from fastapi import status

from presentation.api.schemas.common import ErrorResponse, APIError

UNAUTHORIZED_RESPONSE = {
    status.HTTP_401_UNAUTHORIZED: {
        "model": ErrorResponse,
        "description": "Требуется аутентификация",
        "content": {
            "application/json": {
                "example": ErrorResponse(
                    error=APIError(
                        code="UNAUTHORIZED",
                        message="Требуется аутентификация для доступа к этому ресурсу.",
                        request_id="5fc62665-8ed9-4abb-80e4-45349b30a941",
                    )
                )
            }
        },
    },
}
