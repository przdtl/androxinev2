from typing import List, Optional, TypeVar, Generic
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from enum import IntEnum


# ------------------------
# ENUMS
# ------------------------
class DayOfWeek(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


# ------------------------
# ERROR SCHEMA
# ------------------------
class ErrorResponse(BaseModel):
    detail: str
    code: str  # CAPS


# ------------------------
# CATEGORY
# ------------------------
class CategorySchema(BaseModel):
    id: UUID
    title: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
