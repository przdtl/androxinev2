from exceptions.common import AppException


class SetNotAccessibleError(AppException):
    CODE = "SET_NOT_ACCESSIBLE"
    MESSAGE = "Подход не найден или не принадлежит пользователю"
