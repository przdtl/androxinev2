from models import Exercise, Category

from sqlalchemy.ext.asyncio.session import AsyncSession


class ExerciseDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_default_for_user(self, user_id: int, categories: list[Category]):
        categories_map = {c.title: c.id for c in categories}

        default_exercises = [
            Exercise(
                user_id=user_id,
                category_id=categories_map["Грудь"],
                title="Жим лёжа",
                short="bench",
            ),
            Exercise(
                user_id=user_id,
                category_id=categories_map["Спина"],
                title="Тяга в наклоне",
                short="pull",
            ),
        ]

        self._session.add_all(default_exercises)
