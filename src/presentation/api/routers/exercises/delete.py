import uuid

from fastapi import APIRouter, HTTPException

from dto.exercises import DeleteExerciseInputDTO
from use_cases.exercises import DeleteExerciseUseCase

from presentation.api.dependencies.auth import UserDep
from presentation.api.dependencies.uow import UOWDep
from presentation.api.schemas.exercises import DeleteExerciseResponse

router = APIRouter()


@router.delete(
    path="/{id}/",
    summary="Удалить упражнение",
    description="Удаляет упражнение по идентификатору",
    response_description="Результат удаления",
    response_model=DeleteExerciseResponse,
)
async def delete_exercise(
    id: uuid.UUID,
    uow: UOWDep,
    user_id: UserDep,
) -> DeleteExerciseResponse:
    dto = DeleteExerciseInputDTO(
        user_id=user_id,
        exercise_id=id,
    )
    use_case = DeleteExerciseUseCase(uow=uow)
    try:
        await use_case.execute(input_dto=dto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return DeleteExerciseResponse()
