import typing

import fastapi
from sqlalchemy import create_engine, orm

from vehicle.core.app.abstraction.handler import Handler
from vehicle.core.app.abstraction.repository import Repository
from vehicle.external.api.configuration.config import get_app_settings


def get_session() -> typing.Iterator[orm.Session]:
    """
    Yield an SQLAlchemy Session object.

    Use the yielded session within a context manager for proper cleanup.

    Yields
    ------
    An SQLAlchemy Session object.
    """
    settings = get_app_settings()
    Session = orm.sessionmaker(
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


def get_handler(handler_type: type[Handler], repo_type: type[Repository]) -> typing.Callable[[Repository], Handler]:
    def _get_handler(repo: typing.Annotated[Repository, fastapi.Depends(get_repository(repo_type))]) -> Handler:
        return handler_type(repo)

    return _get_handler


def get_repository(repo_type: type[Repository]) -> typing.Callable[[orm.Session], Repository]:
    def _get_repository(session: typing.Annotated[orm.Session, fastapi.Depends(get_session)]) -> Repository:
        return repo_type(session)

    return _get_repository
