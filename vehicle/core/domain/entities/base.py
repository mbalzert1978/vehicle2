import abc
import dataclasses
import typing

from ..valueobjects.base import ValueObject

TV = typing.TypeVar("TV")


@dataclasses.dataclass
class Entity(abc.ABC):
    id: ValueObject

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, type(self)):
            return self.id == __value.id
        return False
