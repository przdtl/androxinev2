import uuid

from pydantic import BaseModel, Field


class CreateCategoryRequest(BaseModel):
    title: str = Field(min_length=1, max_length=100)


class CreateCategoryResponse(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True
