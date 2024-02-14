import typing
from collections.abc import Sequence

from sqlalchemy import Row, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from vehicle.core.domain.shared.error import Error
from vehicle.core.domain.shared.result import Err, Ok, Result


class SQLAQueryRepository:
    SELECT = """
        SELECT *
        FROM vehicles;
        """

    def __init__(self, session: Session) -> None:
        self._session = session

    def get(self) -> Result[Sequence[Row[typing.Any]], Error]:
        try:
            return Ok(self._session.execute(text(self.SELECT)).fetchall())
        except SQLAlchemyError as exc:
            return Err(Error(500, str(exc)))
