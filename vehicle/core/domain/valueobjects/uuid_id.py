import dataclasses
import typing
import uuid

from .base import ValueObject


@dataclasses.dataclass(frozen=True)
class UuidID(ValueObject[uuid.UUID]):
    value: uuid.UUID

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def create(cls) -> typing.Self:
        return cls(uuid.uuid4())
