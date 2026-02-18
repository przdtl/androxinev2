import uuid
import datetime

from pydantic import BaseModel, Field

from ..common import CategorySchema, DayOfWeek


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
    default_weight: float | None = Field(default=None, gt=0)
    default_reps: int | None = Field(default=None, gt=0)
    order: int | None = None
    exercise: ExerciseSchema

    class Config:
        from_attributes = True


class WorkoutTemplateSchema(BaseModel):
    id: uuid.UUID
    title: str
    day_of_week: DayOfWeek | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    exercises: list[TemplateExerciseSchema] = Field(default_factory=list)

    class Config:
        from_attributes = True


class ListTemplatesResponse(WorkoutTemplateSchema):
    pass
