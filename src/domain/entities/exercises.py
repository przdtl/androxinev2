import uuid
import datetime


class Category:
    def __init__(
        self,
        id: uuid.UUID,
        title: str,
        created_at: datetime.datetime,
        updated_at: datetime.datetime,
    ):
        self._id = id
        self._title = title
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def created_at(self) -> datetime.datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime.datetime:
        return self._updated_at

    def update_title(self, new_title: str) -> None:
        self._updated_at = datetime.datetime.now(tz=datetime.timezone.utc)
        self._title = new_title


class Exercise:
    def __init__(
        self,
        id: uuid.UUID,
        title: str,
        category: Category,
        user_id: int | None,
        short: str,
        created_at: datetime.datetime,
        updated_at: datetime.datetime,
    ):
        self._id = id
        self._title = title
        self._category = category
        self._user_id = user_id
        self._short = short
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def category(self) -> Category:
        return self._category

    @property
    def user_id(self) -> int | None:
        return self._user_id

    @property
    def short(self) -> str:
        return self._short

    @property
    def created_at(self) -> datetime.datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime.datetime:
        return self._updated_at

    def update_title(self, new_title: str) -> None:
        self._updated_at = datetime.datetime.now(tz=datetime.timezone.utc)
        self._title = new_title

    def update_short(self, new_short: str) -> None:
        self._updated_at = datetime.datetime.now(tz=datetime.timezone.utc)
        self._short = new_short

    def belongs_to_category(self, category_id: uuid.UUID) -> bool:
        return self._category.id == category_id
