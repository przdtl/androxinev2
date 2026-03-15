from exceptions.common import AppException


class CategoryNotFoundError(AppException):
    CODE = "CATEGORY_NOT_FOUND"
    MESSAGE = "Категория не найдена"
