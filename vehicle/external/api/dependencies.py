import typing

import fastapi
from sqlalchemy import create_engine
from sqlalchemy import orm as sorm

from ...core.app.services import vehicle_service as service
from ...core.configuration.config import get_app_settings
from ...core.domain.repositories.vehicle_repository import VehicleRepository
from ..persistence.repositories.vehicle_repo import SQLAVehicleRepository


def get_session() -> typing.Iterator[sorm.Session]:
    """
    Yield an SQLAlchemy Session object.

    Use the yielded session within a context manager for proper cleanup.

    Yields
    ------
    An SQLAlchemy Session object.
    """
    settings = get_app_settings()
    Session = sorm.sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=create_engine(
            str(settings.database_url),
            pool_pre_ping=True,
            echo=settings.debug,
        ),
    )
    try:
        session = Session()
        yield session
    finally:
        session.close()


def get_vehicle_repository(
    session: typing.Annotated[sorm.Session, fastapi.Depends(get_session)],
) -> VehicleRepository:
    return SQLAVehicleRepository(session)


def get_vehicle_service(
    repository: typing.Annotated[
        VehicleRepository, fastapi.Depends(get_vehicle_repository)
    ],
) -> service.VehicleService:
    return service.VehicleService(repository)


VehicleService = typing.Annotated[
    service.VehicleService, fastapi.Depends(get_vehicle_service)
]
