import typing

from vehicle.core.app.abstraction.command import Command
from vehicle.core.app.abstraction.repository import Repository

_RV = typing.TypeVar("_RV")
_Repo_co = typing.TypeVar("_Repo_co", bound=Repository, covariant=True)


class Handler(typing.Protocol[_Repo_co]):
    def handle(self, command: Command[_RV]) -> _RV:
        ...
