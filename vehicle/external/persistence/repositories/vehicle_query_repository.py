import typing
from collections.abc import Sequence

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from vehicle.core.app.abstraction.repository import RowLike, SessionLike
from vehicle.core.domain.shared.error import Error


class SQLAQueryRepository:
    SELECT = """
        SELECT *
        FROM vehicles;
        """

    def __init__(self, session: SessionLike) -> None:
        self._session = session

    def get(self) -> Sequence[RowLike[typing.Any]]:
        try:
            return self._session.execute(text(self.SELECT)).fetchall()
        except SQLAlchemyError as exc:
            raise Error.from_exception(exc) from exc
