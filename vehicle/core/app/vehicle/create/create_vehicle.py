from vehicle.core.app.vehicle.create.create_vehicle_command import CreateVehicleCommand
from vehicle.core.domain.shared.error import Error
from vehicle.core.domain.shared.result import Err, Ok, Result
from vehicle.core.domain.shared.value_object import ValueObject
from vehicle.core.domain.vehicle.vehicle import Vehicle
from vehicle.core.domain.vehicle.vehicle_repository import VehicleRepository


class CreateVehicleHandler:
    def __init__(self, vehicle_repository: VehicleRepository) -> None:
        self._vehicle_repository = vehicle_repository

    def handle(self, cmd: CreateVehicleCommand) -> Result[ValueObject, Error]:
        match result := Vehicle.create(
            cmd.name,
            cmd.year_of_manufacture,
            cmd.extras,
            ready_to_drive=cmd.ready_to_drive,
        ):
            case Ok(_vehicle):
                try:
                    with self._vehicle_repository as repo:
                        repo.add(_vehicle)
                except Exception as exc:
                    return Err(Error(500, str(exc)))
                return Ok(_vehicle.id)
            case Err(_):
                return result
