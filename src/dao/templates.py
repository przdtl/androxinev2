from sqlalchemy.ext.asyncio.session import AsyncSession


class WorkoutTemplatesDAO:
    def __init__(self, session: AsyncSession):
        self._session = session
