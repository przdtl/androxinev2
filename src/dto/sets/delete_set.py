import uuid

from pydantic import BaseModel


class DeleteSetInputDTO(BaseModel):
    id: uuid.UUID


class DeleteSetOutputDTO(BaseModel):
    pass
