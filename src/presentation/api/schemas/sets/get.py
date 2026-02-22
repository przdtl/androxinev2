import uuid

from pydantic import BaseModel

from presentation.api.schemas.common import CategorySchema


class ExerciseSchema(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    is_archived: bool

    class Config:
        from_attributes = True


class GetSetResponse(BaseModel):
    id: uuid.UUID
    user_id: int
    exercise: ExerciseSchema
    weight: float
    reps: int

    class Config:
        from_attributes = True
