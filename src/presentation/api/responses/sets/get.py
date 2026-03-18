from fastapi import status

from exceptions.sets import SetNotAccessibleError

from presentation.api.responses.auth import UNAUTHORIZED_RESPONSE
from presentation.api.schemas.common import APIError, ErrorResponse


GET_SET_RESPONSES = {
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorResponse,
        "description": "Подход не найден или недоступен",
        "content": {
            "application/json": {
                "example": ErrorResponse(
                    error=APIError(
                        code=SetNotAccessibleError.CODE,
                        message=SetNotAccessibleError.MESSAGE,
                        request_id="5fc62665-8ed9-4abb-80e4-45349b30a941",
                    )
                )
            }
        },
    },
}

GET_SET_RESPONSES.update(UNAUTHORIZED_RESPONSE)
