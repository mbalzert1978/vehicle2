import http

import pydantic
from fastapi import exceptions
from starlette.requests import Request
from starlette.responses import JSONResponse

ValidationError = exceptions.RequestValidationError | pydantic.ValidationError


async def http422_error_handler(_: Request, exc: ValidationError) -> JSONResponse:
    return JSONResponse(status_code=http.HTTPStatus.UNPROCESSABLE_ENTITY, content=dict(exc))  # TODO Fix me
