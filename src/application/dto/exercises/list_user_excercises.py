import datetime
import uuid

from pydantic import BaseModel


class ListUserExercisesInputDTO(BaseModel):
    page: int
    size: int


class CategorySchema(BaseModel):
    id: uuid.UUID
    title: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


class ListUserExercisesOutputDTO(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_archived: bool

    class Config:
        from_attributes = True
