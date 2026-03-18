from fastapi import status

from exceptions.exercises import ExerciseNotAccessibleError

from presentation.api.responses.auth import UNAUTHORIZED_RESPONSE
from presentation.api.schemas.common import APIError, ErrorResponse


DELETE_EXERCISE_RESPONSES = {
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorResponse,
        "description": "Упражнение не найдено или недоступно",
        "content": {
            "application/json": {
                "example": ErrorResponse(
                    error=APIError(
                        code=ExerciseNotAccessibleError.CODE,
                        message=ExerciseNotAccessibleError.MESSAGE,
                        request_id="5fc62665-8ed9-4abb-80e4-45349b30a941",
                    )
                )
            }
        },
    },
}

DELETE_EXERCISE_RESPONSES.update(UNAUTHORIZED_RESPONSE)
