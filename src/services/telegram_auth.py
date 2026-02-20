from aiogram.utils.web_app import safe_parse_webapp_init_data

from dto.telegram import TelegramInitDataDTO


class TelegramAuthService:
    def __init__(self, bot_token: str):
        self._bot_token = bot_token

    def validate_init_data(self, init_data: str) -> TelegramInitDataDTO | None:
        try:
            data = safe_parse_webapp_init_data(
                token=self._bot_token,
                init_data=init_data,
            )
        except Exception:
            return None

        if not data.user:
            return None

        return TelegramInitDataDTO(
            telegram_id=data.user.id,
            first_name=data.user.first_name,
            last_name=data.user.last_name,
            username=data.user.username,
            photo_url=data.user.photo_url,
        )
