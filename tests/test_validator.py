import pytest
from configguard import Schema, Field, validate
from configguard.errors import ValidationError

schema = Schema({
    'host': Field(type=str, required=True),
    'port': Field(type=int, required=True, min=1, max=65535)
})

def test_valid_config():
    validate({'host': 'localhost', 'port': 5432}, schema)

def test_wrong_type():
    with pytest.raises(ValidationError):
        validate({'host': 'localhost', 'port': 'hello'}, schema)

def test_missing_required_field():
    with pytest.raises(ValidationError):
        validate({'host': 'localhost'}, schema)