import typing
import uuid

from vehicle.core.app.abstraction.repository import SessionLike
from vehicle.core.domain.shared.value_object import ValueObject
from vehicle.core.domain.vehicle.vehicle import Vehicle
from vehicle.external.persistence.mapping.vehicle import VehicleInDB


class SQLAVehicleRepository:
    def __init__(self, session: SessionLike) -> None:
        self._session = session

    def __enter__(self) -> typing.Self:
        return self

    def __exit__(self, exc_type, exc_val, _) -> None:
        if exc_type is not None:
            self._session.rollback()
            raise exc_type(exc_val)
        self._session.commit()

    def add(self, vehicle: Vehicle) -> ValueObject[uuid.UUID]:
        to_add = VehicleInDB(**vehicle.dump())
        self._session.add(to_add)
        return vehicle.id

    def get_by_id(self, vehicle_id: ValueObject) -> Vehicle | None:
        if (result := self._session.get(VehicleInDB, str(vehicle_id))) is None:
            return None
        return Vehicle(**result.dump())

    def update(self, vehicle: Vehicle) -> None:
        to_update = VehicleInDB(**vehicle.dump())
        self._session.merge(to_update)
