import typing
import uuid

from vehicle.core.domain.shared.value_object import ValueObject
from vehicle.core.domain.vehicle.vehicle import Vehicle


class VehicleRepository(typing.Protocol):
    def __enter__(self) -> typing.Self:
        ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ...

    def add(self, vehicle: Vehicle) -> ValueObject[uuid.UUID]:
        ...

    def get_by_id(self, vehicle_id: ValueObject) -> Vehicle | None:
        ...

    def update(self, vehicle: Vehicle) -> None:
        ...
