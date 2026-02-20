from pydantic import BaseModel


class TelegramInitDataDTO(BaseModel):
    telegram_id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None
    photo_url: str | None = None
