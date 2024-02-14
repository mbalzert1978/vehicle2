import dataclasses
import typing

from vehicle.core.domain.shared.entity import Entity
from vehicle.core.domain.shared.error import Error
from vehicle.core.domain.shared.result import Err, Ok, Result

from .uuid_id import UuidID


@dataclasses.dataclass
class Vehicle(Entity):
    id: UuidID
    name: str
    year_of_manufacture: int
    body: dict[str, typing.Any]
    ready_to_drive: bool

    def dump(self) -> dict[str, typing.Any]:
        dump = dataclasses.asdict(self)
        dump.pop("_domain_events")
        dump["id"] = str(self.id)
        return dump

    @classmethod
    def create(
        cls, name: str, year_of_manufacture: int, body: dict[str, typing.Any], *, ready_to_drive: bool
    ) -> Result[typing.Self, Error]:
        match result := UuidID.create():
            case Ok(id):
                return Ok(cls(id, name, year_of_manufacture, body, ready_to_drive))
            case Err(_):
                return result
