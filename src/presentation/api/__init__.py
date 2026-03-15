from . import exception_handlers  # noqa: F401

from .app import app

from .routers import router

app.include_router(router)
