import datetime
import uuid

from pydantic import BaseModel


class ListSetsInputDTO(BaseModel):
    user_id: int
    page: int
    size: int
    exercise_id: uuid.UUID | None = None
    created_from: datetime.datetime | None = None
    created_to: datetime.datetime | None = None


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


class ListSetsOutputDTO(BaseModel):
    id: uuid.UUID
    user_id: int
    exercise: ExerciseSchema
    weight: float
    reps: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
