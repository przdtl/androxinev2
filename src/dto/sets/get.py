import uuid

from pydantic import BaseModel


class GetSetInputDTO(BaseModel):
    user_id: int
    set_id: uuid.UUID


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


class GetSetOutputDTO(BaseModel):
    id: uuid.UUID
    user_id: int
    exercise: ExerciseSchema
    weight: float
    reps: int

    class Config:
        from_attributes = True
