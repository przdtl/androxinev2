from fastapi import APIRouter

from .create import router as create_router
from .delete import router as delete_router
from .get_today_templates import router as get_today_templates_router
from .list import router as list_router
from .update import router as update_router


router = APIRouter(
    prefix="/templates",
    tags=["Шаблоны тренировок"],
)

router.include_router(create_router)
router.include_router(delete_router)
router.include_router(get_today_templates_router)
router.include_router(list_router)
router.include_router(update_router)

__all__ = [
    "router",
]
