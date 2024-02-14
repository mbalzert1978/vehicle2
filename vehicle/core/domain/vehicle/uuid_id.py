import dataclasses
import typing
import uuid

from vehicle.core.domain.shared.result import Err, Ok, Result
from vehicle.core.domain.shared.value_object import ValueObject

from .uuid_error import UUIDError


@dataclasses.dataclass(frozen=True)
class UuidID(ValueObject[uuid.UUID]):
    value: uuid.UUID

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def create(cls) -> Result[typing.Self, UUIDError]:
        try:
            _uuid = uuid.uuid4()
        except Exception as exc:
            return Err(UUIDError(500, str(exc)))
        return Ok(cls(_uuid))
