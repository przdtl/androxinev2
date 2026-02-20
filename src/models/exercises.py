import uuid

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class Category(Base):
    __tablename__ = "category"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
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

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str]
    category_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("category.id", ondelete="SET NULL")
    )
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE")
    )
    short: Mapped[str] = mapped_column(nullable=False)
    is_archived: Mapped[bool] = mapped_column(default=False)

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
