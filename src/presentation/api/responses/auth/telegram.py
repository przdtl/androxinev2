from fastapi import status

from exceptions.account import InvalidTelegramAuthDataError

from presentation.api.schemas.common import APIError, ErrorResponse


TELEGRAM_AUTH_RESPONSES = {
    status.HTTP_400_BAD_REQUEST: {
        "model": ErrorResponse,
        "description": "Некорректные данные Telegram WebApp",
        "content": {
            "application/json": {
                "example": ErrorResponse(
                    error=APIError(
                        code=InvalidTelegramAuthDataError.CODE,
                        message=InvalidTelegramAuthDataError.MESSAGE,
                        request_id="5fc62665-8ed9-4abb-80e4-45349b30a941",
                    )
                )
            }
        },
    },
}
