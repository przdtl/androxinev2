import uuid

from pydantic import BaseModel


class DeleteTemplateInputDTO(BaseModel):
    id: uuid.UUID


class DeleteTemplateOutputDTO(BaseModel):
    pass
