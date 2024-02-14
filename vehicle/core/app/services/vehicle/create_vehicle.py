import typing

from vehicle.core.domain.shared.error import Error
from vehicle.core.domain.shared.result import Err, Ok, Result
from vehicle.core.domain.shared.value_object import ValueObject
from vehicle.core.domain.vehicle.vehicle import Vehicle
from vehicle.core.domain.vehicle.vehicle_repository import VehicleRepository


class CreateVehicleHandler:
    def __init__(self, vehicle_repository: VehicleRepository) -> None:
        self._vehicle_repository = vehicle_repository

    def handle(
        self,
        name: str,
        year_of_manufacture: int,
        body: dict[str, typing.Any],
        *,
        ready_to_drive: bool,
    ) -> Result[ValueObject, Error]:
        match result := Vehicle.create(name, year_of_manufacture, body, ready_to_drive=ready_to_drive):
            case Ok(_vehicle):
                with self._vehicle_repository as repo:
                    repo.add(_vehicle)
                return Ok(_vehicle.id)
            case Err(_):
                return result
