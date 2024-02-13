import typing

import fastapi
from api.core.config import get_app_settings


class ServiceExampleInterface(typing.Protocol):
    def get_value(self) -> dict[str, typing.Any]:
        ...


class ServiceExample:
    def get_value(self) -> dict[str, typing.Any]:
        return {
            "first_name": "John",
            "last_name": "Dow",
            "email": "j@d.com",
            "password": "jd123456",
        }


def get_service_example() -> ServiceExampleInterface:
    return ServiceExample()


Service = typing.Annotated[
    ServiceExampleInterface,
    fastapi.Depends(get_service_example),
]
