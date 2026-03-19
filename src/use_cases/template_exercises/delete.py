from dto.template_exercises import (
    DeleteTemplateExerciseInputDTO,
    DeleteTemplateExerciseOutputDTO,
)
from exceptions.exercises import ExerciseNotFoundError
from exceptions.templates import TemplateAccessDeniedError

from uow import UnitOfWork


class DeleteTemplateExerciseUseCase:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(
        self,
        input_dto: DeleteTemplateExerciseInputDTO,
    ) -> DeleteTemplateExerciseOutputDTO:
        template = await self._uow.workout_templates_dao.get_by_user_and_id(
            user_id=input_dto.user_id,
            template_id=input_dto.template_id,
        )
        if template is None:
            raise TemplateAccessDeniedError(
                context={
                    "template_id": str(input_dto.template_id),
                    "user_id": str(input_dto.user_id),
                }
            )

        template_exercise = await self._uow.workout_templates_dao.get_exercise(
            template_id=input_dto.template_id,
            exercise_id=input_dto.exercise_id,
        )
        if template_exercise is None:
            raise ExerciseNotFoundError(
                context={"exercise_id": str(input_dto.exercise_id)}
            )

        await self._uow.workout_templates_dao.delete_exercise(
            template_id=input_dto.template_id,
            exercise_id=input_dto.exercise_id,
        )

        return DeleteTemplateExerciseOutputDTO()
