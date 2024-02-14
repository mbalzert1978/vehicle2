import typing

from vehicle.core.app.abstraction.command import Command
from vehicle.core.app.abstraction.repository import Repository
from vehicle.core.domain.shared.error import Error
from vehicle.core.domain.shared.result import Result

T_co = typing.TypeVar("T_co", covariant=True)


class Handler(typing.Protocol[T_co]):
    def __init__(self, repository: Repository) -> None:
        ...

    def handle(self, command: Command) -> Result[T_co, Error]:
        ...
