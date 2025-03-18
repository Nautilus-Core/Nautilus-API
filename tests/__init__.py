import os
import pytest
from sqlalchemy import create_engine
from your_module import DATABASE_URL  # Adjust the import according to your project structure

def test_database_url_is_set():
    assert DATABASE_URL is not None, "DATABASE_URL should not be None"

def test_create_engine_with_valid_url():
    if DATABASE_URL:
        engine = create_engine(DATABASE_URL)
        assert engine is not None, "Engine should be created with a valid DATABASE_URL"

def test_create_engine_with_none_url():
    original_database_url = DATABASE_URL
    try:
        os.environ['DATABASE_URL'] = 'None'
        with pytest.raises(Exception) as excinfo:
            create_engine(os.environ['DATABASE_URL'])
        assert "Expected string or URL object, got None" in str(excinfo.value)
    finally:
        os.environ['DATABASE_URL'] = original_database_url  # Restore original value