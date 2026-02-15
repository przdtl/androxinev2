import uuid

from pydantic import BaseModel


class DeleteTemplateExerciseInputDTO(BaseModel):
    id: uuid.UUID


class DeleteTemplateExerciseOutputDTO(BaseModel):
    pass
