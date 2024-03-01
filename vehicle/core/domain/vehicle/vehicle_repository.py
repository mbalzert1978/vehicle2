import typing

from vehicle.core.app.abstraction.repository import Repository
from vehicle.core.domain.shared.value_object import ValueObject
from vehicle.core.domain.vehicle.vehicle import Vehicle

_RV_co = typing.TypeVar("_RV_co", covariant=True)


class VehicleRepository(Repository[_RV_co], typing.Protocol):
    def __enter__(self) -> typing.Self:
        ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ...

    def add(self, vehicle: Vehicle) -> _RV_co:
        ...

    def get_by_id(self, vehicle_id: ValueObject) -> Vehicle | None:
        ...

    def update(self, vehicle: Vehicle) -> None:
        ...
