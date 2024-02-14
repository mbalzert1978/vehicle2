import typing

from sqlalchemy.orm import Session

from ....core.domain.entities.vehicle import Vehicle
from ....core.domain.valueobjects.base import ValueObject
from ..mapping.vehicle import VehicleInDB


class SQLAVehicleRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def __enter__(self) -> typing.Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            self._session.rollback()
            raise exc_type(exc_val)
        self._session.commit()

    def add(self, vehicle: Vehicle) -> ValueObject:
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

    def list(self) -> list[Vehicle]:
        return [
            Vehicle(**vehicle.dump())
            for vehicle in self._session.query(VehicleInDB).all()
        ]
