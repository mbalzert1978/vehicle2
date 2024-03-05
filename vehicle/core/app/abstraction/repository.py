import typing
from collections.abc import Sequence

_RV_co = typing.TypeVar("_RV_co", covariant=True)
_Row_co = typing.TypeVar("_Row_co", covariant=True, bound="RowLike")
_TP_co = typing.TypeVar("_TP_co", covariant=True, bound=tuple[typing.Any, ...])

_Exe_contra = typing.TypeVar("_Exe_contra", contravariant=True)

_O = typing.TypeVar("_O", bound=object)
_P = typing.ParamSpec("_P")


class RowLike(typing.Protocol[_TP_co]):
    ...


class ResultLike(typing.Protocol[_Row_co]):
    def fetchall(self) -> Sequence[_Row_co]:
        ...


class Repository(typing.Protocol[_RV_co]):
    def __enter__(self) -> typing.Self:
        ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ...


class SessionLike(typing.Protocol[_O, _P]):
    def execute(self, statement: _Exe_contra) -> ResultLike[_Row_co]:
        ...

    def add(self, instance: object) -> None:
        ...

    def rollback(self) -> None:
        ...

    def commit(self) -> None:
        ...

    def get(self, entity: type[_O], ident: typing.Any, *args: _P.args, **kwargs: _P.kwargs) -> _O | None:
        ...

    def merge(self, instance: _O, *args: _P.args, **kwargs: _P.kwargs) -> _O:
        ...
