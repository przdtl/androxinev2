import uuid
import datetime

from pydantic import BaseModel, Field

from presentation.api.v1.schemas.common import CategorySchema


class CreateExerciseRequest(BaseModel):
    title: str = Field(min_length=1)
    short: str = Field(min_length=1, max_length=10)
    category_id: uuid.UUID


class CreateExerciseResponse(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_archived: bool

    class Config:
        from_attributes = True
