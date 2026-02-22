import uuid

from pydantic import BaseModel


class CreateExerciseInputDTO(BaseModel):
    user_id: int
    title: str
    short: str
    category_id: uuid.UUID


class CategorySchema(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True


class CreateExerciseOutputDTO(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    is_archived: bool

    class Config:
        from_attributes = True
