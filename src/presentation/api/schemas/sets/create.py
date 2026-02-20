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


class CreateSetRequest(BaseModel):
    exercise_id: uuid.UUID
    weight: float = Field(gt=0)
    reps: int = Field(gt=0)


class CreateSetResponse(BaseModel):
    id: uuid.UUID
    user_id: int
    exercise: ExerciseSchema
    weight: float
    reps: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
