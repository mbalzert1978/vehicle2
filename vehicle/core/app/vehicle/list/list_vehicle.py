import typing
from collections.abc import Sequence

from sqlalchemy import Row

from vehicle.core.app.vehicle.list.list_vehicle_command import ListVehicleCommand
from vehicle.core.domain.shared.error import Error
from vehicle.core.domain.shared.result import Result
from vehicle.core.domain.vehicle.query_repository import VehicleQueryRepository


class ListVehicleHandler:
    def __init__(self, vehicle_repository: VehicleQueryRepository) -> None:
        self._vehicle_repository = vehicle_repository

    def handle(self, _: ListVehicleCommand) -> Result[Sequence[Row[typing.Any]], Error]:
        return self._vehicle_repository.get()
