import typing

from vehicle.core.app.abstraction.repository import Repository

_RV_co = typing.TypeVar("_RV_co", covariant=True)


class VehicleQueryRepository(Repository[_RV_co], typing.Protocol):
    def get(self) -> _RV_co:
        ...
