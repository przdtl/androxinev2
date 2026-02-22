import uuid

from pydantic import BaseModel, Field

from presentation.api.schemas.common import CategorySchema


class ExerciseSchema(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    is_archived: bool

    class Config:
        from_attributes = True


class UpdateSetRequest(BaseModel):
    weight: float | None = Field(default=None, ge=0)
    reps: int | None = Field(default=None, ge=0)


class UpdateSetResponse(BaseModel):
    id: uuid.UUID
    user_id: int
    exercise: ExerciseSchema
    weight: float
    reps: int

    class Config:
        from_attributes = True
