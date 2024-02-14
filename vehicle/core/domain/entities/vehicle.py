import dataclasses
import typing

from ..valueobjects.uuid_id import UuidID
from .base import Entity


@dataclasses.dataclass
class Vehicle(Entity):
    id: UuidID
    name: str
    year_of_manufacture: int
    body: dict[str, typing.Any]
    ready_to_drive: bool

    def dump(self) -> dict[str, typing.Any]:
        dump = dataclasses.asdict(self)
        dump["id"] = str(self.id)
        return dump
