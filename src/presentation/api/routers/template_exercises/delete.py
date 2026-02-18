import uuid

from fastapi import APIRouter

from dto.template_exercises.delete_template_exercise import (
    DeleteTemplateExerciseInputDTO,
)
from use_cases.template_exercises.delete import (
    DeleteTemplateExerciseUseCase,
)

from ..schemas.template_exercises import (
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
) -> DeleteTemplateExerciseResponse:
    dto = DeleteTemplateExerciseInputDTO(id=id)
    use_case = DeleteTemplateExerciseUseCase()
    await use_case.execute(input_dto=dto)

    return DeleteTemplateExerciseResponse()
