import uuid
import enum
import datetime

from pydantic import BaseModel


class DayOfWeek(enum.IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class ErrorResponse(BaseModel):
    detail: str
    code: str


class CategorySchema(BaseModel):
    id: uuid.UUID
    title: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True
