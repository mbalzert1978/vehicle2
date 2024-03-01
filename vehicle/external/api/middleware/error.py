from starlette.requests import Request
from starlette.responses import JSONResponse

from vehicle.core.domain.shared.error import Error


async def error_handler(_: Request, exc: Error) -> JSONResponse:
    return JSONResponse(status_code=exc._code, content=str(exc))
