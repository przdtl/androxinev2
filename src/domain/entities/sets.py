import uuid
import datetime


class Set:
    def __init__(
        self,
        id: uuid.UUID,
        user_id: int,
        exercise_id: uuid.UUID,
        weight: float,
        reps: int,
        created_at: datetime.datetime,
    ):
        self._id = id
        self._user_id = user_id
        self._exercise_id = exercise_id
        self._weight = weight
        self._reps = reps
        self._created_at = created_at

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def exercise_id(self) -> uuid.UUID:
        return self._exercise_id

    @property
    def weight(self) -> float:
        return self._weight

    @property
    def reps(self) -> int:
        return self._reps

    @property
    def created_at(self) -> datetime.datetime:
        return self._created_at

    def performed_today(self) -> bool:
        today = datetime.datetime.now().date()
        return self._created_at.date() == today

    def volume(self) -> float:
        return self._weight * self._reps
