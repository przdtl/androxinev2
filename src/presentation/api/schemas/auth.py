from pydantic import BaseModel, Field


class TelegramAuthRequest(BaseModel):
    init_data: str = Field(
        ...,
        min_length=1,
        description="Telegram WebApp initData string",
    )


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
