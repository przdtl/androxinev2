from exceptions.common import AppException


class CategoryNotAccessibleError(AppException):
    CODE = "CATEGORY_NOT_ACCESSIBLE"
    MESSAGE = "Категория не найдена или не принадлежит пользователю"
