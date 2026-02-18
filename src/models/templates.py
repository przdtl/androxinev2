import enum
import uuid


from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class DayOfWeek(enum.IntEnum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6


class WorkoutTemplate(Base):
    __tablename__ = "workout_template"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    title: Mapped[str]
    day_of_week: Mapped[DayOfWeek | None]

    exercises: Mapped[list["TemplateExercise"]] = relationship(
        backref="workout_template",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "title",
            name="uq_workout_template_user_id_title",
        ),
    )


class TemplateExercise(Base):
    __tablename__ = "template_exercise"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    workout_template_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("workout_template.id")
    )
    exercise_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("exercise.id"))
    weight: Mapped[float | None]
    reps: Mapped[int | None]
    order: Mapped[int] = mapped_column(default=0)

    __table_args__ = (
        UniqueConstraint(
            "workout_template_id",
            "order",
            name="uq_template_exercise_workout_template_id_order",
        ),
    )
