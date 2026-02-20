from sqlalchemy.ext.asyncio.session import AsyncSession


class SetsDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_set_by_id(self, set_id: int):
        pass
