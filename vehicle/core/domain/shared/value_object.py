import dataclasses
import typing

TV = typing.TypeVar("TV")


@dataclasses.dataclass(frozen=True)
class ValueObject(typing.Protocol[TV]):
    value: TV

    def __hash__(self) -> int:
        if isinstance(self.value, typing.Iterable):
            return hash(hash(v) for v in self.value)
        return hash(self.value)

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, self.__class__) and self.value == __value.value
