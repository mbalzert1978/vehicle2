import typing

from sqlalchemy import JSON, Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class VehicleInDB(Base):
    __tablename__ = "vehicles"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    year_of_manufacture: Mapped[int] = mapped_column(Integer)
    body: Mapped[dict[str, typing.Any]] = mapped_column(JSON())
    ready_to_drive: Mapped[bool] = mapped_column(Boolean())

    def dump(self) -> dict[str, typing.Any]:
        return self.__dict__
