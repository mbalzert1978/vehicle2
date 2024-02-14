import typing

import pydantic

T = typing.TypeVar("T")


class DataResponse(pydantic.BaseModel, typing.Generic[T]):
    data: list[T]
