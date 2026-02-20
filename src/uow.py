from sqlalchemy.ext.asyncio import AsyncSession

from dao import CategoryDAO, ExerciseDAO, UsersDAO, WorkoutTemplatesDAO, SetsDAO


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self._session = session

        self.categories_dao = CategoryDAO(session)
        self.exercises_dao = ExerciseDAO(session)
        self.users_dao = UsersDAO(session)
        self.workout_templates_dao = WorkoutTemplatesDAO(session)
        self.sets_dao = SetsDAO(session)

    async def __aenter__(self):
        self._tx = await self._session.begin()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self._tx.rollback()
        else:
            await self._tx.commit()
