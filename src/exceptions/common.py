from typing import Any


class AppException(Exception):
    CODE = "APP_ERROR"
    MESSAGE = "Ошибка приложения"

    def __init__(
        self,
        *,
        code: str | None = None,
        message: str | None = None,
        context: dict[str, Any] | None = None,
    ):
        resolved_code = code or self.CODE
        resolved_message = message or self.MESSAGE

        super().__init__(resolved_message)
        self.code = resolved_code
        self.message = resolved_message
        self.context = context or {}
