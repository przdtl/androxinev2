import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from models import Exercise, Category


class ExerciseDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, exercise_id: uuid.UUID) -> Exercise | None:
        result = await self._session.execute(
            select(Exercise).where(Exercise.id == exercise_id)
        )
        return result.scalar_one_or_none()

    async def get_by_user_and_id(
        self, user_id: int, exercise_id: uuid.UUID
    ) -> Exercise | None:
        result = await self._session.execute(
            select(Exercise).where(
                Exercise.user_id == user_id, Exercise.id == exercise_id
            )
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        user_id: int,
        title: str,
        short: str,
        category_id: uuid.UUID,
    ) -> Exercise:
        result = await self._session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = result.scalar_one()

        exercise = Exercise(
            user_id=user_id,
            title=title,
            short=short,
            category=category,
        )
        self._session.add(exercise)
        await self._session.flush()
        return exercise

    async def update(
        self,
        exercise_id: uuid.UUID,
        title: str | None = None,
        short: str | None = None,
        category_id: uuid.UUID | None = None,
    ) -> Exercise:
        exercise = await self.get_by_id(exercise_id)
        if not exercise:
            raise ValueError(f"Exercise {exercise_id} not found")

        if title is not None:
            exercise.title = title
        if short is not None:
            exercise.short = short
        if category_id is not None:
            exercise.category_id = category_id

        await self._session.flush()
        return exercise

    async def archive(self, exercise_id: uuid.UUID) -> Exercise:
        exercise = await self.get_by_id(exercise_id)
        if not exercise:
            raise ValueError(f"Exercise {exercise_id} not found")

        exercise.is_archived = True
        await self._session.flush()
        return exercise

    async def restore(self, exercise_id: uuid.UUID) -> Exercise:
        exercise = await self.get_by_id(exercise_id)
        if not exercise:
            raise ValueError(f"Exercise {exercise_id} not found")

        exercise.is_archived = False
        await self._session.flush()
        return exercise

    async def delete(self, exercise_id: uuid.UUID) -> None:
        exercise = await self.get_by_id(exercise_id)
        if not exercise:
            raise ValueError(f"Exercise {exercise_id} not found")

        await self._session.delete(exercise)
        await self._session.flush()

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

    async def list_by_user_id(
        self,
        user_id: int,
        page: int,
        size: int,
        is_archived: bool | None = None,
    ) -> list[Exercise]:
        offset = (page - 1) * size
        query = select(Exercise).where(Exercise.user_id == user_id)

        if is_archived is not None:
            query = query.where(Exercise.is_archived == is_archived)

        result = await self._session.execute(query.offset(offset).limit(size))
        return result.scalars().all()

    async def count_by_user_id(
        self, user_id: int, is_archived: bool | None = None
    ) -> int:
        query = select(Exercise).where(Exercise.user_id == user_id)

        if is_archived is not None:
            query = query.where(Exercise.is_archived == is_archived)

        result = await self._session.execute(query)
        return len(result.scalars().all())
