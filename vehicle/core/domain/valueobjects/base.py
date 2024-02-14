import dataclasses
import typing

TV = typing.TypeVar("TV")


@dataclasses.dataclass(frozen=True)
class ValueObject(typing.Protocol[TV]):
    value: TV

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, type(self)):
            return self.value == __value.value
        return False
