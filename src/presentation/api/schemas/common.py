import uuid
import enum

from pydantic import BaseModel, Field


class DayOfWeek(enum.IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class ErrorDetail(BaseModel):
    field: str | None = None
    code: str
    message: str


class APIError(BaseModel):
    code: str
    message: str
    details: list[ErrorDetail] = Field(default_factory=list)
    request_id: str | None = None


class ErrorResponse(BaseModel):
    error: APIError


class CategorySchema(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True
