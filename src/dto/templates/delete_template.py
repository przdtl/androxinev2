import uuid

from pydantic import BaseModel


class DeleteTemplateInputDTO(BaseModel):
    user_id: int
    id: uuid.UUID


class DeleteTemplateOutputDTO(BaseModel):
    pass
