import json

from sqlalchemy import text
from sqlalchemy.orm import Session

from vehicle.core.domain.vehicle.vehicle import Vehicle
from vehicle.external.persistence.repositories.vehicle_repo import SQLAVehicleRepository


def test_create(session: Session):
    """
    Given: A empty database session
    When: Creating a new vehicle using the Repository
    Then: The vehicle should be added to the database and the
        vehicle should be returned with a valid id.
    """
    to_add = Vehicle.create(
        name="test_name",
        year_of_manufacture=2024,
        extras={"test": "body"},
        ready_to_drive=True,
    )

    with SQLAVehicleRepository(session) as repo:
        _id = repo.add(to_add)

    sql = text("SELECT * FROM vehicles WHERE id=:id").bindparams(id=str(_id))

    sql_result = session.execute(sql).one()

    assert sql_result.id == str(_id)
    assert sql_result.name == to_add.name
    assert sql_result.year_of_manufacture == to_add.year_of_manufacture
    assert sql_result.extras == json.dumps(to_add.extras)
    assert sql_result.ready_to_drive == to_add.ready_to_drive
