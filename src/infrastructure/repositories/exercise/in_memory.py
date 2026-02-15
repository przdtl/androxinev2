import uuid

from application.repositories.exercise import ExerciseRepository
from domain.entities.exercises import Exercise


class InMemoryExerciseRepository(ExerciseRepository):
    def __init__(self):
        self._storage: dict[uuid.UUID, Exercise] = {}

    async def add(self, exercise: Exercise) -> None:
        self._storage[exercise.id] = exercise

    async def remove(self, exercise_id: uuid.UUID) -> None:
        if exercise_id in self._storage:
            del self._storage[exercise_id]

    async def get(self, exercise_id: uuid.UUID) -> Exercise | None:
        return self._storage.get(exercise_id)

    async def exists(self, exercise_id: uuid.UUID) -> bool:
        return exercise_id in self._storage

    async def list(self) -> list[Exercise]:
        return list(self._storage.values())
