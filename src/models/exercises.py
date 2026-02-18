import uuid

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class Category(Base):
    __tablename__ = "category"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    title: Mapped[str]

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "title",
            name="uq_category_user_id_title",
        ),
    )


class Exercise(Base):
    __tablename__ = "exercise"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    category_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("category.id"))
    user_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"))
    short: Mapped[str]
    is_archived: Mapped[bool]

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "title",
            name="uq_exercise_user_id_title",
        ),
        UniqueConstraint(
            "user_id",
            "short",
            name="uq_exercise_user_id_short",
        ),
    )
