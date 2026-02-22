import datetime
import uuid

from pydantic import BaseModel


class GetExerciseInputDTO(BaseModel):
    exercise_id: uuid.UUID
    user_id: int


class CategorySchema(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True


class GetExerciseOutputDTO(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    is_archived: bool

    class Config:
        from_attributes = True
