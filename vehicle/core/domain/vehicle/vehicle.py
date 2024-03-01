import dataclasses
import typing

from vehicle.core.domain.shared.entity import Entity
from vehicle.core.domain.vehicle.uuid_id import UuidID


@dataclasses.dataclass
class Vehicle(Entity):
    id: UuidID
    name: str
    year_of_manufacture: int
    extras: dict[str, typing.Any]
    ready_to_drive: bool

    def dump(self) -> dict[str, typing.Any]:
        dump = dataclasses.asdict(self)
        dump.pop("_domain_events")
        dump["id"] = str(self.id)
        return dump

    @classmethod
    def create(
        cls,
        name: str,
        year_of_manufacture: int,
        extras: dict[str, typing.Any],
        *,
        ready_to_drive: bool,
    ) -> typing.Self:
        return cls(UuidID.create(), name, year_of_manufacture, extras, ready_to_drive)
