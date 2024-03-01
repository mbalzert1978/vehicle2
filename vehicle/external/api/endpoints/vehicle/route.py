"""FastAPI vehicles module."""
import typing
from collections.abc import Sequence

import fastapi
from sqlalchemy import Row

from vehicle.core.app.abstraction.handler import Handler
from vehicle.core.app.vehicle.create.create_vehicle import CreateVehicleHandler
from vehicle.core.app.vehicle.create.create_vehicle_command import CreateVehicleCommand
from vehicle.core.app.vehicle.list.list_vehicle import ListVehicleHandler
from vehicle.core.app.vehicle.list.list_vehicle_command import ListVehicleCommand
from vehicle.core.domain.shared.value_object import ValueObject
from vehicle.external.api.dependencies import get_handler
from vehicle.external.api.models.data_response import DataResponse
from vehicle.external.api.models.vehicle_response import VehicleResponse
from vehicle.external.persistence.repositories.vehicle_query_repository import SQLAQueryRepository
from vehicle.external.persistence.repositories.vehicle_repo import SQLAVehicleRepository

UNREACHABLE = "Unreachable error."
vehicle = fastapi.APIRouter(prefix="/vehicles")


@vehicle.get("/", name="list:vehicles")
def list_vehicles(
    handler: typing.Annotated[
        Handler,
        fastapi.Depends(get_handler(ListVehicleHandler, SQLAQueryRepository)),
    ],
) -> DataResponse[VehicleResponse]:
    rows = handler.handle(ListVehicleCommand[Sequence[Row[typing.Any]]]())
    return DataResponse(data=[VehicleResponse.model_validate(row) for row in rows])


@vehicle.post("/", name="create:vehicle")
def create_vehicle(
    handler: typing.Annotated[
        Handler,
        fastapi.Depends(get_handler(CreateVehicleHandler, SQLAVehicleRepository)),
    ],
    name: str,
    year_of_manufacture: int,
    extras: dict[str, typing.Any],
    ready_to_drive: bool,
) -> DataResponse[str]:
    cmd = CreateVehicleCommand[ValueObject](
        name=name,
        year_of_manufacture=year_of_manufacture,
        extras=extras,
        ready_to_drive=ready_to_drive,
    )
    return DataResponse(data=[str(handler.handle(cmd))])
