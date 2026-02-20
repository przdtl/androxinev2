import uuid
import datetime

from pydantic import BaseModel

from presentation.api.schemas.common import CategorySchema


class ExerciseSchema(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_archived: bool

    class Config:
        from_attributes = True


class TemplateExerciseSchema(BaseModel):
    id: uuid.UUID
    default_weight: float | None
    default_reps: int | None
    order: int | None
    exercise: ExerciseSchema

    class Config:
        from_attributes = True


class ListTemplateExercisesResponse(TemplateExerciseSchema):
    pass
