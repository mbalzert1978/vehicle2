"""Vehicle api."""
from fastapi import FastAPI

# from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware

from vehicle.external.api.configuration.config import get_app_settings
from vehicle.external.api.configuration.events import (
    create_start_app_handler,
    create_stop_app_handler,
)
from vehicle.external.api.endpoints.vehicle.route import vehicle

# from ..api.middleware import error_handler, http422_error_handler


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

    # application.add_exception_handler(Error, error_handler)
    # application.add_exception_handler(RequestValidationError, http422_error_handler)
    # TODO: create Error handler for all exceptions
    application.include_router(vehicle, prefix=settings.api_prefix)

    return application


app = get_application()
