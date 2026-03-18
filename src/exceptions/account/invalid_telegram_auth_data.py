from exceptions.common import AppException


class InvalidTelegramAuthDataError(AppException):
    CODE = "AUTH_INVALID_TELEGRAM_DATA"
    MESSAGE = "Некорректные данные аутентификации Telegram"
