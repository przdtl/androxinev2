import uuid
import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class Set(Base):
    __tablename__ = "set"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    exercise_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("exercise.id"))
    weight: Mapped[float]
    reps: Mapped[int]
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now)
    updated_at: Mapped[datetime.datetime | None] = mapped_column(
        default=None,
        onupdate=datetime.datetime.now,
    )
