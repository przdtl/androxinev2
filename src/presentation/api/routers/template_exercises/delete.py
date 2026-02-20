import uuid

from fastapi import APIRouter

from dto.template_exercises.delete_template_exercise import (
    DeleteTemplateExerciseInputDTO,
)
from use_cases.template_exercises.delete import (
    DeleteTemplateExerciseUseCase,
)

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.template_exercises import (
    DeleteTemplateExerciseResponse,
)

router = APIRouter()


@router.delete(
    path="/{id}/",
    summary="Удалить упражнение из шаблона",
    description="Удаляет упражнение из шаблона по идентификатору",
    response_description="Результат удаления",
    response_model=DeleteTemplateExerciseResponse,
)
async def delete_template_excercise(
    id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> DeleteTemplateExerciseResponse:
    dto = DeleteTemplateExerciseInputDTO(id=id)
    use_case = DeleteTemplateExerciseUseCase(uow=uow)
    await use_case.execute(input_dto=dto)

    return DeleteTemplateExerciseResponse()
