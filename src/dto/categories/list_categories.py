import datetime
import uuid

from pydantic import BaseModel


class ListCategoriesInputDTO(BaseModel):
    page: int
    size: int


class ListCategoriesOutputDTO(BaseModel):
    id: uuid.UUID
    title: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True
