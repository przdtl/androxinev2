import uuid

from fastapi import APIRouter, status

from dto.template_exercises.delete_template_exercise import (
    DeleteTemplateExerciseInputDTO,
)
from use_cases.template_exercises.delete import (
    DeleteTemplateExerciseUseCase,
)

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep

router = APIRouter()


@router.delete(
    path="/{exercise_id}/",
    summary="Удалить упражнение из шаблона",
    description="Удаляет упражнение из шаблона по идентификатору",
    response_description="Результат удаления",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_template_excercise(
    template_id: uuid.UUID,
    exercise_id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> None:
    dto = DeleteTemplateExerciseInputDTO(
        user_id=user_id,
        template_id=template_id,
        exercise_id=exercise_id,
    )
    use_case = DeleteTemplateExerciseUseCase(uow=uow)
    await use_case.execute(input_dto=dto)
