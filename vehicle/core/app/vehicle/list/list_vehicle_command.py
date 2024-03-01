import dataclasses
import typing

from vehicle.core.app.abstraction.command import Command

_RV = typing.TypeVar("_RV")


@dataclasses.dataclass(frozen=True)
class ListVehicleCommand(Command[_RV]):
    ...
