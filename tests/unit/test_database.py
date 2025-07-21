import os
import sys
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

def test_database_url_uses_environment_variable(monkeypatch):
    """Tests that the DATABASE_URL is read from the environment if set."""
    test_url = "postgresql://user:pass@host:5432/testdb"
    monkeypatch.setenv("DATABASE_URL", test_url)

    if 'app.operations.database' in sys.modules:
        del sys.modules['app.operations.database']
    from app.operations.database import DATABASE_URL, engine

    assert DATABASE_URL == test_url
    # FIX: Compare attributes of the URL object, not the redacted string
    assert engine.url.username == "user"
    assert engine.url.password == "pass"
    assert engine.url.host == "host"
    assert engine.url.database == "testdb"

def test_database_url_uses_default_value(monkeypatch):
    """Tests that a default URL is used when the environment variable is not set."""
    monkeypatch.delenv("DATABASE_URL", raising=False)

    if 'app.operations.database' in sys.modules:
        del sys.modules['app.operations.database']
    from app.operations.database import DATABASE_URL, engine

    default_url = "postgresql://postgres:postgres@db:5432/fastapi_db"
    assert DATABASE_URL == default_url
    # FIX: Compare attributes of the URL object
    assert engine.url.username == "postgres"
    assert engine.url.password == "postgres"
    assert engine.url.host == "db"
    assert engine.url.database == "fastapi_db"

def test_database_objects_have_correct_types():
    """Verifies that the created SQLAlchemy objects are of the correct type."""
    from app.operations.database import engine, SessionLocal, Base
    assert isinstance(engine, Engine)
    assert isinstance(SessionLocal, sessionmaker)
    # Check if Base is a declarative base class
    assert hasattr(Base, 'metadata')