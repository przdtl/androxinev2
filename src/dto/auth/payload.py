from pydantic import BaseModel


class PayloadDataDTO(BaseModel):
    telegram_id: int


class PayloadDTO(BaseModel):
    sub: str
    iat: int
    exp: int
