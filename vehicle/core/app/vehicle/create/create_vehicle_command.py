import dataclasses
import typing

from vehicle.core.app.abstraction.command import Command

_RV = typing.TypeVar("_RV")


@dataclasses.dataclass(frozen=True)
class CreateVehicleCommand(Command[_RV]):
    name: str
    year_of_manufacture: int
    ready_to_drive: bool
    extras: dict[str, typing.Any] = dataclasses.field(default_factory=dict)
