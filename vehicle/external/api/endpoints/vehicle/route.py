"""FastAPI vehicles module."""
import fastapi

from .....core.domain.entities.vehicle import Vehicle
from ...dependencies import VehicleService
from ...models.response import DataResponse

router = fastapi.APIRouter()


@router.get("/", name="get:vehicle")
def get_vehicle(service: VehicleService) -> DataResponse[Vehicle]:
    return DataResponse(data=service.list())
