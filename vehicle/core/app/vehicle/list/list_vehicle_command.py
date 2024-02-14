import dataclasses

from vehicle.core.app.abstraction.command import Command


@dataclasses.dataclass(frozen=True)
class ListVehicleCommand(Command):
    ...
