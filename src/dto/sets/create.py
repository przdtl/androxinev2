import datetime
import uuid

from pydantic import BaseModel


class CreateSetInputDTO(BaseModel):
    user_id: int
    exercise_id: uuid.UUID
    weight: float
    reps: int


class CategorySchema(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True


class ExerciseSchema(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    is_archived: bool

    class Config:
        from_attributes = True


class CreateSetOutputDTO(BaseModel):
    id: uuid.UUID
    user_id: int
    exercise: ExerciseSchema
    weight: float
    reps: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
