from dto.auth import (
    TelegramAuthInputDTO,
    TelegramAuthOutputDTO,
)
from services.jwt import JWTService
from services.telegram_auth import TelegramAuthService


class TelegramAuthUseCase:
    def __init__(
        self,
        telegram_auth_service: TelegramAuthService,
        jwt_service: JWTService,
    ):
        self._telegram_auth_service = telegram_auth_service
        self._jwt_service = jwt_service

    async def execute(
        self,
        input_dto: TelegramAuthInputDTO,
    ) -> TelegramAuthOutputDTO:
        return TelegramAuthOutputDTO(
            access_token="fasdfas",
            token_type="bearer",
        )
