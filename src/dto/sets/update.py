import uuid

from pydantic import BaseModel


class UpdateSetInputDTO(BaseModel):
    user_id: int
    set_id: uuid.UUID
    weight: float | None = None
    reps: int | None = None


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


class UpdateSetOutputDTO(BaseModel):
    id: uuid.UUID
    user_id: int
    exercise: ExerciseSchema
    weight: float
    reps: int

    class Config:
        from_attributes = True
