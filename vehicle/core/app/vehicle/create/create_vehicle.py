from vehicle.core.app.vehicle.create.create_vehicle_command import CreateVehicleCommand
from vehicle.core.domain.shared.value_object import ValueObject
from vehicle.core.domain.vehicle.vehicle import Vehicle
from vehicle.core.domain.vehicle.vehicle_repository import VehicleRepository


class CreateVehicleHandler:
    def __init__(self, vehicle_repository: VehicleRepository) -> None:
        self._vehicle_repository = vehicle_repository

    def handle(self, cmd: CreateVehicleCommand) -> ValueObject:
        _vehicle = Vehicle.create(cmd.name, cmd.year_of_manufacture, cmd.extras, ready_to_drive=cmd.ready_to_drive)
        with self._vehicle_repository as repo:
            repo.add(_vehicle)
        return _vehicle.id
