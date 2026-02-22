import uuid

from pydantic import BaseModel


class CreateCategoryInputDTO(BaseModel):
    user_id: int
    title: str


class CreateCategoryOutputDTO(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True
