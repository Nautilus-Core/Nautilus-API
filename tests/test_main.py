import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import ArgumentError

def test_database_url_set():
    database_url = os.getenv('DATABASE_URL')
    assert database_url is not None, "DATABASE_URL should be set"

def test_create_engine_with_valid_url():
    database_url = "sqlite:///:memory:"
    engine = create_engine(database_url)
    assert engine is not None

def test_create_engine_with_none_url():
    with pytest.raises(ArgumentError, match="Expected string or URL object, got None"):
        create_engine(None)