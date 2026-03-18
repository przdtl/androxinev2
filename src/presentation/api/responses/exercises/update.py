from fastapi import status

from exceptions.exercises import ExerciseAccessDeniedError, ExerciseNotFoundError

from presentation.api.responses.auth import UNAUTHORIZED_RESPONSE
from presentation.api.schemas.common import APIError, ErrorResponse


UPDATE_EXERCISE_RESPONSES = {
    status.HTTP_403_FORBIDDEN: {
        "model": ErrorResponse,
        "description": "Нет доступа к упражнению",
        "content": {
            "application/json": {
                "example": ErrorResponse(
                    error=APIError(
                        code=ExerciseAccessDeniedError.CODE,
                        message=ExerciseAccessDeniedError.MESSAGE,
                        request_id="5fc62665-8ed9-4abb-80e4-45349b30a941",
                    )
                )
            }
        },
    },
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorResponse,
        "description": "Упражнение не найдено",
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

UPDATE_EXERCISE_RESPONSES.update(UNAUTHORIZED_RESPONSE)
