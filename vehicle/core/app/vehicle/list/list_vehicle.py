import typing
from collections.abc import Sequence

from vehicle.core.app.abstraction.repository import RowLike
from vehicle.core.app.vehicle.list.list_vehicle_command import ListVehicleCommand
from vehicle.core.domain.vehicle.query_repository import VehicleQueryRepository


class ListVehicleHandler:
    def __init__(self, vehicle_repository: VehicleQueryRepository) -> None:
        self._vehicle_repository = vehicle_repository

    def handle(self, _: ListVehicleCommand) -> Sequence[RowLike[typing.Any]]:
        return self._vehicle_repository.get()
