from models import User

from dto.auth import TelegramAuthInputDTO, TelegramAuthOutputDTO, PayloadDataDTO

from services.jwt import JWTService
from services.telegram_auth import TelegramAuthService

from uow import UnitOfWork


class InvalidTelegramAuthDataError(Exception):
    def __init__(self):
        super().__init__("Invalid Telegram authentication data")


class TelegramAuthUseCase:
    def __init__(
        self,
        uow: UnitOfWork,
        telegram_auth_service: TelegramAuthService,
        jwt_service: JWTService,
    ):
        self._telegram_auth_service = telegram_auth_service
        self._jwt_service = jwt_service
        self._uow = uow

    async def execute(
        self,
        input_dto: TelegramAuthInputDTO,
    ) -> TelegramAuthOutputDTO:
        telegram_user = self._telegram_auth_service.validate_init_data(
            input_dto.init_data
        )
        if not telegram_user:
            raise InvalidTelegramAuthDataError()

        user = await self._get_or_create_user(telegram_user)

        token = self._jwt_service.encode(data=PayloadDataDTO(telegram_id=user.id))

        return TelegramAuthOutputDTO(
            access_token=token,
            token_type="bearer",
        )

    async def _get_or_create_user(self, telegram_user) -> User:
        user = await self._uow.users_dao.get_by_id(
            telegram_id=telegram_user.telegram_id,
        )
        if not user:
            user = await self._uow.users_dao.create(
                telegram_id=telegram_user.telegram_id,
                first_name=telegram_user.first_name,
                last_name=telegram_user.last_name,
                username=telegram_user.username,
                photo_url=telegram_user.photo_url,
            )
            await self._initialize_user_defaults(user.id)
        else:
            await self._uow.users_dao.update(
                telegram_id=telegram_user.telegram_id,
                first_name=telegram_user.first_name,
                last_name=telegram_user.last_name,
                username=telegram_user.username,
                photo_url=telegram_user.photo_url,
            )

        return user

    async def _initialize_user_defaults(self, user_id: int):
        categories = await self._uow.categories_dao.create_default_for_user(user_id)
        await self._uow.exercises_dao.create_default_for_user(
            user_id=user_id,
            categories=categories,
        )
