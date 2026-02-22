import uuid

from pydantic import BaseModel


class GetCategoryResponse(BaseModel):
    id: uuid.UUID
    title: str

    class Config:
        from_attributes = True
