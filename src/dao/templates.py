import uuid

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from models import TemplateExercise, WorkoutTemplate


class WorkoutTemplatesDAO:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, template_id: uuid.UUID) -> WorkoutTemplate | None:
        result = await self._session.execute(
            select(WorkoutTemplate).where(WorkoutTemplate.id == template_id)
        )
        return result.scalar_one_or_none()

    async def get_by_user_and_id(
        self,
        user_id: int,
        template_id: uuid.UUID,
    ) -> WorkoutTemplate | None:
        result = await self._session.execute(
            select(WorkoutTemplate).where(
                WorkoutTemplate.user_id == user_id,
                WorkoutTemplate.id == template_id,
            )
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        user_id: int,
        title: str,
        day_of_week: int | None,
    ) -> WorkoutTemplate:
        template = WorkoutTemplate(
            user_id=user_id,
            title=title,
            day_of_week=day_of_week,
        )
        self._session.add(template)
        await self._session.flush()
        return template

    async def update(
        self,
        template_id: uuid.UUID,
        title: str | None = None,
        day_of_week: int | None = None,
    ) -> WorkoutTemplate:
        template = await self.get_by_id(template_id=template_id)
        if title is not None:
            template.title = title
        if day_of_week is not None:
            template.day_of_week = day_of_week

        await self._session.flush()
        return template

    async def delete(self, template_id: uuid.UUID) -> None:
        template = await self.get_by_id(template_id=template_id)
        if template is not None:
            await self._session.delete(template)
            await self._session.flush()

    async def list_by_user_id(
        self,
        user_id: int,
        page: int,
        size: int,
    ) -> list[WorkoutTemplate]:
        offset = (page - 1) * size
        result = await self._session.execute(
            select(WorkoutTemplate)
            .where(WorkoutTemplate.user_id == user_id)
            .order_by(WorkoutTemplate.id.desc())
            .offset(offset)
            .limit(size)
        )
        return result.scalars().all()

    async def list_by_user_and_day(
        self,
        user_id: int,
        day_of_week: int,
    ) -> list[WorkoutTemplate]:
        result = await self._session.execute(
            select(WorkoutTemplate)
            .where(
                WorkoutTemplate.user_id == user_id,
                WorkoutTemplate.day_of_week == day_of_week,
            )
            .order_by(WorkoutTemplate.id.desc())
        )
        return result.scalars().all()

    async def list_exercises(
        self,
        template_id: uuid.UUID,
        page: int,
        size: int,
    ) -> list[TemplateExercise]:
        offset = (page - 1) * size
        result = await self._session.execute(
            select(TemplateExercise)
            .where(TemplateExercise.workout_template_id == template_id)
            .order_by(TemplateExercise.order.asc())
            .offset(offset)
            .limit(size)
        )
        return result.scalars().all()

    async def list_exercises_all(self, template_id: uuid.UUID) -> list[TemplateExercise]:
        result = await self._session.execute(
            select(TemplateExercise)
            .where(TemplateExercise.workout_template_id == template_id)
            .order_by(TemplateExercise.order.asc())
        )
        return result.scalars().all()

    async def get_exercise(
        self,
        template_id: uuid.UUID,
        exercise_id: uuid.UUID,
    ) -> TemplateExercise | None:
        result = await self._session.execute(
            select(TemplateExercise).where(
                TemplateExercise.workout_template_id == template_id,
                TemplateExercise.exercise_id == exercise_id,
            )
        )
        return result.scalar_one_or_none()

    async def get_next_exercise_order(self, template_id: uuid.UUID) -> int:
        result = await self._session.execute(
            select(func.max(TemplateExercise.order)).where(
                TemplateExercise.workout_template_id == template_id
            )
        )
        max_order = result.scalar_one_or_none()
        return 0 if max_order is None else max_order + 1

    async def create_exercise(
        self,
        template_id: uuid.UUID,
        exercise_id: uuid.UUID,
        default_weight: float | None,
        default_reps: int | None,
        order: int,
    ) -> TemplateExercise:
        template_exercise = TemplateExercise(
            workout_template_id=template_id,
            exercise_id=exercise_id,
            weight=default_weight,
            reps=default_reps,
            order=order,
        )
        self._session.add(template_exercise)
        await self._session.flush()
        return template_exercise

    async def update_exercise(
        self,
        template_id: uuid.UUID,
        exercise_id: uuid.UUID,
        default_weight: float | None = None,
        default_reps: int | None = None,
    ) -> TemplateExercise | None:
        template_exercise = await self.get_exercise(
            template_id=template_id,
            exercise_id=exercise_id,
        )
        if template_exercise is None:
            return None

        if default_weight is not None:
            template_exercise.weight = default_weight
        if default_reps is not None:
            template_exercise.reps = default_reps

        await self._session.flush()
        return template_exercise

    async def delete_exercise(
        self,
        template_id: uuid.UUID,
        exercise_id: uuid.UUID,
    ) -> None:
        template_exercise = await self.get_exercise(
            template_id=template_id,
            exercise_id=exercise_id,
        )
        if template_exercise is not None:
            await self._session.delete(template_exercise)
            await self._session.flush()
