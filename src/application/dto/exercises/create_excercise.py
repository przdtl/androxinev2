import uuid

from pydantic import BaseModel


class CreateExerciseInputDTO(BaseModel):
    title: str
    short: str
    category_id: uuid.UUID


class CreateExerciseOutputDTO(BaseModel):
    pass
