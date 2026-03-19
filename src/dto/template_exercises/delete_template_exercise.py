import uuid

from pydantic import BaseModel


class DeleteTemplateExerciseInputDTO(BaseModel):
    user_id: int
    template_id: uuid.UUID
    exercise_id: uuid.UUID


class DeleteTemplateExerciseOutputDTO(BaseModel):
    pass
