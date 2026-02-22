import uuid

from pydantic import BaseModel


class GetCategoryInputDTO(BaseModel):
    user_id: int
    category_id: uuid.UUID


class GetCategoryOutputDTO(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True
