import uuid

from pydantic import BaseModel


class DeleteSetInputDTO(BaseModel):
    set_id: uuid.UUID
    user_id: int


class DeleteSetOutputDTO(BaseModel):
    pass
