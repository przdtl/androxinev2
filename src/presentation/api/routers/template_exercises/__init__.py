from fastapi import APIRouter

from .create import router as create_router
from .update import router as update_router
from .delete import router as delete_router


router = APIRouter(
    prefix="/templates/{template_id}/exercises",
    tags=["Упражнения в шаблонах"],
)

router.include_router(create_router)
router.include_router(update_router)
router.include_router(delete_router)

__all__ = [
    "router",
]
