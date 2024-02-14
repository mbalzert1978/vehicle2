import typing

from ..entities.vehicle import Vehicle
from ..valueobjects.base import ValueObject


class VehicleRepository(typing.Protocol):
    def __enter__(self) -> typing.Self:
        ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ...

    def add(self, vehicle: Vehicle) -> ValueObject:
        ...

    def get_by_id(self, vehicle_id: ValueObject) -> Vehicle | None:
        ...

    def update(self, vehicle: Vehicle) -> None:
        ...
