import dataclasses
import typing

_RV = typing.TypeVar("_RV")


@dataclasses.dataclass(frozen=True)
class Command(typing.Generic[_RV]):
    ...
