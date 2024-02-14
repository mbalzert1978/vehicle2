import typing

import fastapi
from sqlalchemy import create_engine
from sqlalchemy import orm as sorm

from vehicle.core.app.queries import vehicle_query as query
from vehicle.core.app.services.vehicle import create_vehicle as service
from vehicle.core.domain.vehicle.vehicle_repository import VehicleRepository
from vehicle.external.api.configuration.config import get_app_settings
from vehicle.external.persistence.repositories.vehicle_repo import SQLAVehicleRepository


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
    repository: typing.Annotated[VehicleRepository, fastapi.Depends(get_vehicle_repository)],
) -> service.CreateVehicleHandler:
    return service.CreateVehicleHandler(repository)


def get_vehicle_query(
    session: typing.Annotated[sorm.Session, fastapi.Depends(get_session)],
) -> query.VehicleQuery:
    return query.VehicleQuery(session)


VehicleService = typing.Annotated[service.CreateVehicleHandler, fastapi.Depends(get_vehicle_service)]

VehicleQuery = typing.Annotated[query.VehicleQuery, fastapi.Depends(get_vehicle_query)]
