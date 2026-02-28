from .bot import dp, setup_webhook, shutdown_webhook, process_update
from .handlers import router

dp.include_router(router)

__all__ = [
    "setup_webhook",
    "shutdown_webhook",
    "process_update",
]
