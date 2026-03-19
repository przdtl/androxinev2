from exceptions.common import AppException


class TemplateAccessDeniedError(AppException):
    CODE = "TEMPLATE_ACCESS_DENIED"
    MESSAGE = "Шаблон тренировки не принадлежит пользователю"
