import uuid

from pydantic import BaseModel


class DeleteCategoryInputDTO(BaseModel):
    user_id: int
    category_id: uuid.UUID


class DeleteCategoryOutputDTO(BaseModel):
    pass
