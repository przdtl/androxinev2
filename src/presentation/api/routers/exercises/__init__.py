from fastapi import APIRouter

from .list import router as list_router
from .create import router as create_router
from .update import router as update_router
from .get import router as get_router
from .archive import router as archive_router
from .restore import router as restore_router

router = APIRouter(
    prefix="/exercises",
    tags=["Упражнения"],
)

router.include_router(list_router)
router.include_router(create_router)
router.include_router(update_router)
router.include_router(get_router)
router.include_router(archive_router)
router.include_router(restore_router)

__all__ = [
    "router",
]
