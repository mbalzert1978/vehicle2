from sqlalchemy import text
from sqlalchemy.orm import Session


class VehicleQuery:
    SELECT = """
            SELECT *
            FROM vehicles;
            """

    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self):
        return self._session.execute(text(self.SELECT)).fetchall()
