import uuid

from pydantic import BaseModel, Field

from presentation.api.schemas.common import CategorySchema


class CreateExerciseRequest(BaseModel):
    category_id: uuid.UUID
    title: str = Field(min_length=1)
    short: str = Field(min_length=1, max_length=10)


class CreateExerciseResponse(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    is_archived: bool

    class Config:
        from_attributes = True
