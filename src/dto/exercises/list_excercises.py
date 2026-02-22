import uuid

from pydantic import BaseModel


class ListExercisesInputDTO(BaseModel):
    user_id: int
    page: int
    size: int


class CategorySchema(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True


class ListExercisesOutputDTO(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    is_archived: bool

    class Config:
        from_attributes = True
