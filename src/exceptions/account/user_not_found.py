from exceptions.common import AppException


class UserNotFoundError(AppException):
    CODE = "USER_NOT_FOUND"
    MESSAGE = "Пользователь не найден"
