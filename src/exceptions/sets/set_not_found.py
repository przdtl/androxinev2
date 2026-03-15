from exceptions.common import AppException


class SetNotFoundError(AppException):
    CODE = "SET_NOT_FOUND"
    MESSAGE = "Подход не найден"
