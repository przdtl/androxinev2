import uuid
import datetime

from pydantic import BaseModel, Field

from presentation.api.schemas.common import CategorySchema, DayOfWeek


class TemplateExerciseCreateInput(BaseModel):
    exercise_id: uuid.UUID
    default_weight: float | None = Field(default=None, gt=0)
    default_reps: int | None = Field(default=None, gt=0)
    order: int | None = None


class CreateTemplateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    day_of_week: DayOfWeek | None = None
    exercises: list[TemplateExerciseCreateInput] = Field(default_factory=list)


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


class CreateTemplateResponse(BaseModel):
    id: uuid.UUID
    title: str
    day_of_week: DayOfWeek | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    exercises: list[TemplateExerciseSchema] = []

    class Config:
        from_attributes = True
