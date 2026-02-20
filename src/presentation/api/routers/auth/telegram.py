from fastapi import APIRouter, status

from dto.auth import TelegramAuthInputDTO

from use_cases.auth import TelegramAuthUseCase

from services.jwt import JWTService
from services.telegram_auth import TelegramAuthService

from config import settings

from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.auth import AuthResponse, TelegramAuthRequest

router = APIRouter()


@router.post(
    "/telegram/",
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK,
    summary="Authenticate via Telegram WebApp",
)
async def telegram_auth(request: TelegramAuthRequest, uow: UOWDep) -> AuthResponse:
    """
    Authenticate user via Telegram WebApp init_data.

    Validates the init_data signature and returns JWT access token.
    """
    input_dto = TelegramAuthInputDTO(init_data=request.init_data)

    telegram_auth_service = TelegramAuthService(bot_token=settings.TELEGRAM_BOT_TOKEN)
    jwt_service = JWTService(
        secret_key=settings.JWT_SECRET_KEY,
        access_token_expire_minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    )

    use_case = TelegramAuthUseCase(
        telegram_auth_service=telegram_auth_service,
        jwt_service=jwt_service,
        uow=uow,
    )

    output_dto = await use_case.execute(input_dto)

    return AuthResponse(
        access_token=output_dto.access_token,
        token_type=output_dto.token_type,
    )
