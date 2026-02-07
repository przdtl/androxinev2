class User:
    def __init__(self, telegram_id: int):
        self._telegram_id = telegram_id

    @property
    def id(self) -> int:
        return self._telegram_id
