"""Buber Dinner api."""
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware

from buberdinner.api.core.config import get_app_settings
from buberdinner.api.core.events import (
    create_start_app_handler,
    create_stop_app_handler,
)
from buberdinner.api.middleware import error_handler, http422_error_handler
from buberdinner.api.v1.controllers import Authcontroller
from buberdinner.app.error import Error


def get_application() -> FastAPI:
    settings = get_app_settings()

    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )

    application.add_exception_handler(Error, error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)
    application.include_router(Authcontroller, prefix=settings.api_prefix)

    return application


app = get_application()
