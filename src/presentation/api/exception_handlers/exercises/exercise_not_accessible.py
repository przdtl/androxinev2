from fastapi import Request, status

from exceptions.exercises import ExerciseNotAccessibleError

from presentation.api.app import app
from presentation.api.exception_handlers.common import app_base_exception_to_error


@app.exception_handler(ExerciseNotAccessibleError)
async def exercise_not_accessible_exception_handler(
    request: Request,
    exc: ExerciseNotAccessibleError,
):
    return app_base_exception_to_error(
        request=request,
        exc=exc,
        status_code=status.HTTP_404_NOT_FOUND,
    )
