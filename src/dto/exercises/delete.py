import uuid

from pydantic import BaseModel


class DeleteExerciseInputDTO(BaseModel):
    user_id: int
    exercise_id: uuid.UUID


class DeleteExerciseOutputDTO(BaseModel):
    pass
