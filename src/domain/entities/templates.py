import uuid
import datetime


from domain.enums import DayOfWeek


class WorkoutTemplate:
    def __init__(
        self,
        id: uuid.UUID,
        user_id: int,
        title: str,
        day_of_week: DayOfWeek | None,
        created_at: datetime.datetime,
        updated_at: datetime.datetime,
        exercises: list["TemplateExercise"],
    ):
        self._id = id
        self._user_id = user_id
        self._title = title
        self._day_of_week = day_of_week
        self._created_at = created_at
        self._updated_at = updated_at
        self._exercises = exercises

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def day_of_week(self) -> DayOfWeek | None:
        return self._day_of_week

    @property
    def created_at(self) -> datetime.datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime.datetime:
        return self._updated_at

    @property
    def exercises(self) -> list["TemplateExercise"]:
        return self._exercises


class TemplateExercise:
    def __init__(
        self,
        id: uuid.UUID,
        exercise_id: int,
        weight: float | None,
        reps: int | None,
        order: int | None,
    ):
        self._id = id
        self._exercise_id = exercise_id
        self._weight = weight
        self._reps = reps
        self._order = order

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def exercise_id(self) -> int:
        return self._exercise_id

    @property
    def default_weight(self) -> float | None:
        return self._weight

    @property
    def default_reps(self) -> int | None:
        return self._reps

    @property
    def order(self) -> int | None:
        return self._order
