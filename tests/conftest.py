from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, StaticPool, create_engine
from sqlalchemy.orm import Session, sessionmaker

from vehicle.external.api.dependencies import get_session
from vehicle.external.api.main import app
from vehicle.external.persistence.mapping.vehicle import Base


@pytest.fixture()
def db_engine() -> Iterator[Engine]:
    engine = create_engine(
        "sqlite:///:memory:",
        echo=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    engine.dispose()


@pytest.fixture()
def session(db_engine) -> Iterator[Session]:
    Session = sessionmaker(bind=db_engine)  # noqa: N806
    session = Session()
    yield session
    session.close()


@pytest.fixture()
def client(session) -> Iterator[TestClient]:
    app.dependency_overrides[get_session] = lambda: session
    with TestClient(app) as c:
        yield c
