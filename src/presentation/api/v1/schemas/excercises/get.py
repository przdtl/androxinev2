import uuid
import datetime

from pydantic import BaseModel

from presentation.api.v1.schemas.common import CategorySchema


class GetExerciseResponse(BaseModel):
    id: uuid.UUID
    title: str
    short: str
    category: CategorySchema
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_archived: bool

    class Config:
        from_attributes = True
