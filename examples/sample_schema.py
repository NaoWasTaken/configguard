from configguard import Schema, Field, validate
from configguard.errors import ValidationError

schema = Schema({
    'host': Field(type=str, required=True),
    'port': Field(type=int, required=True, min=1, max=65535),
    'username': Field(type=str, required=True)
})

config = {'host': 'localhost', 'port': 5432, 'username': 'admin'}

try:
    validate(config, schema)
    print("Config is valid!")
except ValidationError as e:
    print(f"Invalid config: {e}")