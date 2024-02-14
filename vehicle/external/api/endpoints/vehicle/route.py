"""FastAPI vehicles module."""
import typing

import fastapi

from ...dependencies import VehicleQuery, VehicleService
from ...models.data_response import DataResponse
from ...models.vehicle_response import VehicleResponse

vehicle = fastapi.APIRouter(prefix="/vehicles")


@vehicle.get("/", name="list:vehicles")
def list_vehicles(query: VehicleQuery) -> DataResponse[VehicleResponse]:
    return DataResponse(
        data=[VehicleResponse.model_validate(r) for r in query.list()]
    )


@vehicle.post("/", name="create:vehicle")
def create_vehicle(
    service: VehicleService,
    name: str,
    year_of_manufacture: int,
    body: dict[str, typing.Any],
    ready_to_drive: bool,
) -> DataResponse[str]:
    return DataResponse(
        data=[
            str(
                service.create(
                    name=name,
                    year_of_manufacture=year_of_manufacture,
                    body=body,
                    ready_to_drive=ready_to_drive,
                )
            )
        ]
    )
