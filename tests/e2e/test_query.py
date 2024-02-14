import json
import typing

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response
from pydantic import ValidationError

from vehicle.core.domain.vehicle.vehicle import Vehicle


def _structural_correctnes(data: Response, model: type[typing.Any]):
    match data.json():
        case {"data": list(extracted)}:
            try:
                model(**extracted.pop(0))
            except ValidationError:
                pytest.fail("Validation failed.")
            else:
                return True
        case _:
            pytest.fail("Structure failed.")


def test_CRUD_happy_path(client: TestClient):
    test_vehicle = {
        "name": "test_vehicle",
        "year_of_manufacture": 2020,
        "ready_to_drive": False,
    }
    extras = {
        "color": "test_color",
        "kilometer": 10,
        "price": 10_000,
        "vehicle_type": "test_type",
    }
    # Create a new vehicle
    create = client.post("/api/vehicles", content=json.dumps(extras), params=test_vehicle)
    assert create.status_code == status.HTTP_200_OK

    # Retrieve vehicles
    get = client.get("/api/vehicles")
    assert get.status_code == status.HTTP_200_OK
    assert _structural_correctnes(get, Vehicle)
