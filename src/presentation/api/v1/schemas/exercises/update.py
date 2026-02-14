import uuid
import datetime

from pydantic import BaseModel, Field

from presentation.api.v1.schemas.common import CategorySchema


class UpdateExerciseRequest(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    short: str | None = Field(default=None, min_length=1, max_length=10)
    is_archived: bool | None = None


class UpdateExerciseResponse(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_archived: bool

    class Config:
        from_attributes = True
