import datetime


def utc_now_aware() -> datetime.datetime:
    """Return current timezone-aware UTC datetime for token timestamps."""
    return datetime.datetime.now(datetime.UTC)


def utc_now_naive() -> datetime.datetime:
    """Return current UTC datetime without tzinfo for DB TIMESTAMP WITHOUT TIME ZONE."""
    return utc_now_aware().replace(tzinfo=None)


def normalize_to_utc_naive(
    value: datetime.datetime | datetime.date | None,
    *,
    default_now: bool = True,
) -> datetime.datetime | None:
    """Normalize date/datetime values to UTC-naive datetime for persistence.

    Rules:
    - None -> current UTC-naive datetime (when default_now=True) or None
    - date -> datetime at 00:00:00 (naive)
    - aware datetime -> converted to UTC and stripped tzinfo
    - naive datetime -> unchanged
    """
    if value is None:
        return utc_now_naive() if default_now else None

    if isinstance(value, datetime.date) and not isinstance(value, datetime.datetime):
        return datetime.datetime.combine(value, datetime.time.min)

    if value.tzinfo is not None:
        return value.astimezone(datetime.UTC).replace(tzinfo=None)

    return value
