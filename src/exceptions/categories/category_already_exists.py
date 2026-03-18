from exceptions.common import AppException


class CategoryAlreadyExistsError(AppException):
    CODE = "CATEGORY_ALREADY_EXISTS"
    MESSAGE = "Категория с таким названием уже существует"
