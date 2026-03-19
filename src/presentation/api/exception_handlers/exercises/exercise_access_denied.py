from fastapi import Request, status

from exceptions.exercises import ExerciseAccessDeniedError

from presentation.api.app import app
from presentation.api.exception_handlers.common import app_base_exception_to_error


@app.exception_handler(ExerciseAccessDeniedError)
async def exercise_access_denied_exception_handler(
    request: Request,
    exc: ExerciseAccessDeniedError,
):
    return app_base_exception_to_error(
        request=request,
        exc=exc,
        status_code=status.HTTP_403_FORBIDDEN,
    )
