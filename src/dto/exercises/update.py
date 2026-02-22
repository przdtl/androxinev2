import uuid

from pydantic import BaseModel


class UpdateExerciseInputDTO(BaseModel):
    exercise_id: uuid.UUID
    user_id: int
    title: str | None = None
    short: str | None = None
    is_archived: bool | None = None


class CategorySchema(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True


class UpdateExerciseOutputDTO(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    is_archived: bool

    class Config:
        from_attributes = True
