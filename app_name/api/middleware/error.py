from starlette.requests import Request
from starlette.responses import JSONResponse

from buberdinner.app.error.common.error import Error

INSTANCE = "Buberdinner"


async def error_handler(_: Request, exc: Error) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content=exc.map_error())
