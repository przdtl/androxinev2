from fastapi import status

from exceptions.categories import CategoryNotAccessibleError

from presentation.api.responses.auth import UNAUTHORIZED_RESPONSE
from presentation.api.schemas.common import APIError, ErrorResponse


UPDATE_CATEGORY_RESPONSES = {
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorResponse,
        "description": "Категория не найдена или недоступна",
        "content": {
            "application/json": {
                "example": ErrorResponse(
                    error=APIError(
                        code=CategoryNotAccessibleError.CODE,
                        message=CategoryNotAccessibleError.MESSAGE,
                        request_id="5fc62665-8ed9-4abb-80e4-45349b30a941",
                    )
                )
            }
        },
    },
}

UPDATE_CATEGORY_RESPONSES.update(UNAUTHORIZED_RESPONSE)
