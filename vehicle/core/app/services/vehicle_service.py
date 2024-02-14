import typing

from ...domain.entities.vehicle import Vehicle
from ...domain.repositories.vehicle_repository import VehicleRepository
from ...domain.valueobjects.base import ValueObject
from ...domain.valueobjects.uuid_id import UuidID


class VehicleService:
    def __init__(self, vehicle_repository: VehicleRepository) -> None:
        self._vehicle_repository = vehicle_repository

    def create(
        self,
        name: str,
        year_of_manufacture: int,
        body: dict[str, typing.Any],
        ready_to_drive: bool,
    ) -> ValueObject:
        with self._vehicle_repository as repo:
            repo.add(
                Vehicle(
                    id=(id := UuidID.create()),
                    name=name,
                    year_of_manufacture=year_of_manufacture,
                    body=body,
                    ready_to_drive=ready_to_drive,
                )
            )
        return id
