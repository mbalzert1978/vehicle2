import typing

T = typing.TypeVar("T")


class Error(Exception):
    def __init__(self, code: int, description: str, *args: object) -> None:
        self._code = code
        self._description = description
        super().__init__(*args)

    @classmethod
    def none(cls) -> typing.Self:
        return cls(code=500, description="Internal Server Error")
