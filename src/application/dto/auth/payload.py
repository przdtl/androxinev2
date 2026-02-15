from pydantic import BaseModel


class PayloadDataDTO(BaseModel):
    telegram_id: int


class PayloadDTO(BaseModel):
    sub: int
    iat: int
    exp: int
