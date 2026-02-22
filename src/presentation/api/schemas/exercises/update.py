import uuid

from pydantic import BaseModel, Field

from presentation.api.schemas.common import CategorySchema


class UpdateExerciseRequest(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    short: str | None = Field(default=None, min_length=1, max_length=10)


class UpdateExerciseResponse(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    is_archived: bool

    class Config:
        from_attributes = True
