import uuid

from fastapi import APIRouter

from application.dto.template_exercises.delete_template_exercise import (
    DeleteTemplateExerciseInputDTO,
)
from application.use_cases.template_exercises.delete import (
    DeleteTemplateExerciseUseCase,
)

from presentation.api.v1.schemas.template_exercises import (
    DeleteTemplateExerciseRequest,
    DeleteTemplateExerciseResponse,
)
from presentation.dependencies.uow import UowDep

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
    data: DeleteTemplateExerciseRequest,
    uow: UowDep,
) -> DeleteTemplateExerciseResponse:
    dto = DeleteTemplateExerciseInputDTO(id=id)
    use_case = DeleteTemplateExerciseUseCase(uow=uow)
    await use_case.execute(input_dto=dto)

    return DeleteTemplateExerciseResponse()
