from fastapi import APIRouter

from .list import router as list_router
from .create import router as create_router
from .delete import router as delete_router


router = APIRouter(
    prefix="/sets",
    tags=["Сеты"],
)

router.include_router(list_router)
router.include_router(create_router)
router.include_router(delete_router)

__all__ = [
    "router",
]
