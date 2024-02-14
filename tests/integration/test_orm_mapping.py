import json

from sqlalchemy import text
from sqlalchemy.orm import Session

from vehicle.external.persistence.mapping.vehicle import VehicleInDB


def test_create_vehicle(session: Session) -> None:
    """
    Given: A database session
    When: Creating a new vehicle
    Then: The vehicle should be added to the database.
    """
    expected = VehicleInDB(
        id="test_id",
        name="test_vehicle",
        year_of_manufacture=2024,
        body={"body": {"color": "blue"}},
        ready_to_drive=True,
    )
    session.add(expected)
    session.commit()

    sql = text("SELECT * FROM vehicles WHERE id=:id").bindparams(id="test_id")
    result = session.execute(sql).one()

    assert result.id == expected.id
    assert result.name == expected.name
    assert result.year_of_manufacture == 2024
    assert result.body == json.dumps(expected.body)
    assert result.ready_to_drive == int(expected.ready_to_drive)
