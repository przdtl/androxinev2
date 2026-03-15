from exceptions.common import AppException


class ExerciseNotFoundError(AppException):
    CODE = "EXERCISE_NOT_FOUND"
    MESSAGE = "Упражнение не найдено"
