from domain.entities.users import User

from application.dto.auth import (
    TelegramAuthInputDTO,
    TelegramAuthOutputDTO,
    PayloadDataDTO,
)
from application.uow import UnitOfWork
from application.services.jwt import JWTService
from application.services.telegram_auth import TelegramAuthService


class TelegramAuthUseCase:
    def __init__(
        self,
        uow: UnitOfWork,
        telegram_auth_service: TelegramAuthService,
        jwt_service: JWTService,
    ):
        self._uow = uow
        self._telegram_auth_service = telegram_auth_service
        self._jwt_service = jwt_service

    async def execute(
        self,
        input_dto: TelegramAuthInputDTO,
    ) -> TelegramAuthOutputDTO:
        validated_data = self._telegram_auth_service.validate_init_data(
            input_dto.init_data
        )
        if not validated_data:
            raise ValueError("Invalid Telegram init_data")

        telegram_id = self._telegram_auth_service.extract_user_id(validated_data)
        if not telegram_id:
            raise ValueError("Cannot extract user_id from init_data")

        user = await self._uow.users_repo.get(telegram_id)
        if not user:
            user = User(telegram_id=telegram_id)
            await self._uow.users_repo.add(user)
            await self._uow.commit()

        token_data = PayloadDataDTO(
            telegram_id=telegram_id,
        )

        access_token = self._jwt_service.create_access_token(data=token_data)

        return TelegramAuthOutputDTO(
            access_token=access_token,
            token_type="bearer",
        )
