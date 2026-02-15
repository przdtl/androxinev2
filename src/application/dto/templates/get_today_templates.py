import datetime
import enum
import uuid

from pydantic import BaseModel


class DayOfWeek(enum.IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class GetTodayTemplatesInputDTO(BaseModel):
    pass


class CategorySchema(BaseModel):
    id: uuid.UUID
    title: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


class ExerciseSchema(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_archived: bool

    class Config:
        from_attributes = True


class TemplateExerciseSchema(BaseModel):
    id: uuid.UUID
    default_weight: float | None = None
    default_reps: int | None = None
    order: int | None = None
    exercise: ExerciseSchema

    class Config:
        from_attributes = True


class GetTodayTemplatesOutputDTO(BaseModel):
    id: uuid.UUID
    title: str
    day_of_week: DayOfWeek | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    exercises: list[TemplateExerciseSchema] = []

    class Config:
        from_attributes = True
