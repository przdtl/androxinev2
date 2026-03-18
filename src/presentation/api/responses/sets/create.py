from fastapi import status

from exceptions.exercises import ExerciseNotFoundError

from presentation.api.responses.auth import UNAUTHORIZED_RESPONSE
from presentation.api.schemas.common import ErrorResponse, APIError


CREATE_SET_RESPONSES = {
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorResponse,
        "description": "Упражнение не найдено или недоступно",
        "content": {
            "application/json": {
                "example": ErrorResponse(
                    error=APIError(
                        code=ExerciseNotFoundError.CODE,
                        message=ExerciseNotFoundError.MESSAGE,
                        request_id="5fc62665-8ed9-4abb-80e4-45349b30a941",
                    )
                )
            }
        },
    },
}

CREATE_SET_RESPONSES.update(UNAUTHORIZED_RESPONSE)
