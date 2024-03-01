import abc
import dataclasses
import typing

from vehicle.core.domain.shared.domain_event import DomainEvent
from vehicle.core.domain.shared.value_object import ValueObject

TV = typing.TypeVar("TV")


@dataclasses.dataclass
class Entity(abc.ABC):
    id: ValueObject
    _domain_events: list[DomainEvent] = dataclasses.field(default_factory=list, init=False)

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Entity) and self.id == __value.id

    def send(self, domain_event: DomainEvent) -> None:
        self._domain_events.append(domain_event)
