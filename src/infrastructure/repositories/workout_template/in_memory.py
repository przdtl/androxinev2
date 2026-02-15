import uuid

from domain.entities.templates import WorkoutTemplate

from application.repositories.workout_template import WorkoutTemplateRepository

storage: dict[uuid.UUID, WorkoutTemplate] = {}


class InMemoryWorkoutTemplateRepository(WorkoutTemplateRepository):
    def __init__(self):
        self._storage: dict[uuid.UUID, WorkoutTemplate] = storage

    async def add(self, template: WorkoutTemplate) -> None:
        self._storage[template.id] = template

    async def remove(self, template_id: uuid.UUID) -> None:
        if template_id in self._storage:
            del self._storage[template_id]

    async def get(self, template_id: uuid.UUID) -> WorkoutTemplate | None:
        return self._storage.get(template_id)

    async def exists(self, template_id: uuid.UUID) -> bool:
        return template_id in self._storage

    async def list(self) -> list[WorkoutTemplate]:
        return list(self._storage.values())
