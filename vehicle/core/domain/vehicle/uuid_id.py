import dataclasses
import typing
import uuid

from vehicle.core.domain.shared.value_object import ValueObject
from vehicle.core.domain.vehicle.uuid_error import UUIDError


@dataclasses.dataclass(frozen=True)
class UuidID(ValueObject[uuid.UUID]):
    value: uuid.UUID

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def create(cls) -> typing.Self:
        try:
            _uuid = uuid.uuid4()
        except ValueError as exc:
            raise UUIDError.from_exception(exc) from exc
        return cls(_uuid)
