from exceptions.common import AppException


class ExerciseAccessDeniedError(AppException):
    CODE = "EXERCISE_ACCESS_DENIED"
    MESSAGE = "Упражнение не принадлежит пользователю"
