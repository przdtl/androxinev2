import datetime

from common import utc_now_naive


def safe_datetime(value: datetime.datetime | None) -> datetime.datetime:
    return value if isinstance(value, datetime.datetime) else utc_now_naive()


def safe_day_of_week(value) -> int | None:
    return int(value) if value is not None else None
