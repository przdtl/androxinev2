from pydantic import BaseModel


class TelegramAuthInputDTO(BaseModel):
    init_data: str


class TelegramAuthOutputDTO(BaseModel):
    access_token: str
    token_type: str
