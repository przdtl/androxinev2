import uuid
import datetime

from pydantic import BaseModel

from ..common import CategorySchema


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


class SetSchema(BaseModel):
    id: uuid.UUID
    user_id: int
    exercise: ExerciseSchema
    weight: float
    reps: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class ListSetsResponse(SetSchema):
    pass
