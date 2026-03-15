from exceptions.common import AppException


class ExerciseNotAccessibleError(AppException):
    CODE = "EXERCISE_NOT_ACCESSIBLE"
    MESSAGE = "Упражнение не найдено или не принадлежит пользователю"
