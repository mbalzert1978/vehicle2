import typing

_TSess_co = typing.TypeVar("_TSess_co", covariant=True)


class Repository(typing.Protocol[_TSess_co]):
    def __init__(self, session: _TSess_co) -> None:
        ...
