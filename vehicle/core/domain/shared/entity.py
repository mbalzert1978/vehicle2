import abc
import dataclasses
import typing

from vehicle.core.domain.shared.value_object import ValueObject

from .domain_event import DomainEvent

TV = typing.TypeVar("TV")


@dataclasses.dataclass
class Entity(abc.ABC):
    id: ValueObject
    _domain_events: list[DomainEvent] = dataclasses.field(default_factory=list, init=False)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, type(self)):
            return self.id == __value.id
        return False

    def send(self, domain_event: DomainEvent) -> None:
        self._domain_events.append(domain_event)
