import datetime
import uuid

from pydantic import BaseModel


class CreateSetByExerciseShortInputDTO(BaseModel):
    user_id: int
    exercise_short: str
    weight: float
    reps: int
    created_at: datetime.datetime


class CreateSetByExerciseShortOutputDTO(BaseModel):
    id: uuid.UUID
    exercise_id: uuid.UUID
    exercise_title: str
    weight: float
    reps: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
