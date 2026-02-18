import datetime
import uuid

from pydantic import BaseModel


class CreateTemplateExerciseInputDTO(BaseModel):
    exercise_id: uuid.UUID
    default_weight: float | None = None
    default_reps: int | None = None
    order: int | None = None


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


class CreateTemplateExerciseOutputDTO(BaseModel):
    id: uuid.UUID
    default_weight: float | None = None
    default_reps: int | None = None
    order: int | None = None
    exercise: ExerciseSchema

    class Config:
        from_attributes = True
