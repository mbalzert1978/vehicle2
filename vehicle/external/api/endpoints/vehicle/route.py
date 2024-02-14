"""FastAPI vehicles module."""
import typing

import fastapi

from vehicle.core.app.abstraction.handler import Handler
from vehicle.core.app.vehicle.create.create_vehicle import CreateVehicleHandler
from vehicle.core.app.vehicle.create.create_vehicle_command import CreateVehicleCommand
from vehicle.core.app.vehicle.list.list_vehicle import ListVehicleHandler
from vehicle.core.app.vehicle.list.list_vehicle_command import ListVehicleCommand
from vehicle.core.domain.shared.result import Err, Ok
from vehicle.core.domain.shared.value_object import ValueObject
from vehicle.external.api.dependencies import get_handler
from vehicle.external.api.models.data_response import DataResponse
from vehicle.external.api.models.vehicle_response import VehicleResponse
from vehicle.external.persistence.repositories.vehicle_query_repository import SQLAQueryRepository
from vehicle.external.persistence.repositories.vehicle_repo import SQLAVehicleRepository

vehicle = fastapi.APIRouter(prefix="/vehicles")


@vehicle.get("/", name="list:vehicles")
def list_vehicles(
    handler: typing.Annotated[Handler, fastapi.Depends(get_handler(ListVehicleHandler, SQLAQueryRepository))],
) -> DataResponse[VehicleResponse]:
    match handler.handle(ListVehicleCommand()):
        case Ok(rows):
            return DataResponse(data=[VehicleResponse.model_validate(r) for r in rows])
        case Err(error):
            raise error
        case _:
            raise fastapi.HTTPException(500, detail="Unreachable error.")


@vehicle.post("/", name="create:vehicle")
def create_vehicle(
    handler: typing.Annotated[
        Handler[ValueObject],
        fastapi.Depends(get_handler(CreateVehicleHandler, SQLAVehicleRepository)),
    ],
    name: str,
    year_of_manufacture: int,
    extras: dict[str, typing.Any],
    ready_to_drive: bool,
) -> DataResponse[str]:
    cmd = CreateVehicleCommand(
        name=name,
        year_of_manufacture=year_of_manufacture,
        extras=extras,
        ready_to_drive=ready_to_drive,
    )
    match handler.handle(cmd):
        case Ok(_id):
            return DataResponse(data=[str(_id)])
        case Err(error):
            raise error
        case _:
            raise fastapi.HTTPException(500, detail="Unreachable error.")
