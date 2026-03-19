import uuid
import datetime

from pydantic import BaseModel, Field

from presentation.api.schemas.common import CategorySchema


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


class UpdateTemplateExerciseRequest(BaseModel):
    default_weight: float | None = Field(default=None, gt=0)
    default_reps: int | None = Field(default=None, gt=0)


class UpdateTemplateExerciseResponse(BaseModel):
    id: uuid.UUID
    default_weight: float | None = None
    default_reps: int | None = None
    exercise: ExerciseSchema

    class Config:
        from_attributes = True
