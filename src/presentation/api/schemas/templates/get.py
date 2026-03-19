import uuid
import datetime

from pydantic import BaseModel

from presentation.api.schemas.common import CategorySchema, DayOfWeek


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


class TemplateResponse(BaseModel):
    id: uuid.UUID
    title: str
    day_of_week: DayOfWeek | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    exercises: list[TemplateExerciseSchema] = []

    class Config:
        from_attributes = True
