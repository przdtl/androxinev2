import uuid

from pydantic import BaseModel


class UpdateCategoryInputDTO(BaseModel):
    user_id: int
    category_id: uuid.UUID
    title: str


class UpdateCategoryOutputDTO(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True
