import uuid

from pydantic import BaseModel


class ListCategoriesInputDTO(BaseModel):
    user_id: int
    page: int
    size: int


class ListCategoriesOutputDTO(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True
