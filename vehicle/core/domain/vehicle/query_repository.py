import typing
from collections.abc import Sequence

from sqlalchemy import Row

from vehicle.core.domain.shared.error import Error
from vehicle.core.domain.shared.result import Result


class VehicleQueryRepository(typing.Protocol):
    def get(self) -> Result[Sequence[Row[typing.Any]], Error]:
        ...
