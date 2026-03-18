import datetime
import uuid

from pydantic import BaseModel


class CreateSetByExerciseShortInputDTO(BaseModel):
    user_id: int
    exercise_short: str
    weight: float
    reps: int
    created_at: datetime.datetime | datetime.date | None = None


class CreateSetByExerciseShortOutputDTO(BaseModel):
    id: uuid.UUID
    exercise_id: uuid.UUID
    exercise_title: str
    weight: float
    reps: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
