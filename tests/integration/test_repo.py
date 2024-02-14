import json

from sqlalchemy import text
from sqlalchemy.orm import Session

from vehicle.core.app.services.vehicle_service import VehicleService
from vehicle.external.persistence.repositories.vehicle_repo import SQLAVehicleRepository


def test_create(session: Session):
    """
    Given: A empty database session
    When: Creating a new vehicle using the Repository
    Then: The vehicle should be added to the database and the
        vehicle should be returned with a valid id.
    """
    to_add = dict(
        name="test_name",
        year_of_manufacture=2024,
        body={"test": "body"},
        ready_to_drive=True,
    )
    
    response = VehicleService(SQLAVehicleRepository(session)).create(**to_add)

    sql = text("SELECT * FROM vehicles WHERE id=:id").bindparams(id=str(response.value))

    result = session.execute(sql).one()

    assert result.id == str(response.value)
    assert result.name == to_add["name"]
    assert result.year_of_manufacture == to_add["year_of_manufacture"]
    assert result.body == json.dumps(to_add["body"])
    assert result.ready_to_drive == to_add["ready_to_drive"]
