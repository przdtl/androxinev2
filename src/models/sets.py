import uuid
import datetime

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class Set(Base):
    __tablename__ = "set"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    exercise_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("exercise.id", ondelete="SET NULL")
    )
    weight: Mapped[float] = mapped_column(nullable=False)
    reps: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now)
    updated_at: Mapped[datetime.datetime | None] = mapped_column(
        default=None,
        onupdate=datetime.datetime.now,
    )

    __table_args__ = (
        CheckConstraint(
            "weight >= 0",
            name="check_weight_non_negative",
        ),
        CheckConstraint(
            "reps >= 0",
            name="check_reps_non_negative",
        ),
    )
