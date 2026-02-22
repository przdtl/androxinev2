from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import Exercise, Category

from db.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    photo_url: Mapped[str | None]

    exercises: Mapped[list["Exercise"]] = relationship(
        back_populates="user", lazy="selectin"
    )
    categories: Mapped[list["Category"]] = relationship(
        back_populates="user", lazy="selectin"
    )
