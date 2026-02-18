# ConfigGuard
A Python library that validates configuration files (YAML, JSON, TOML) against a schema, catching errors before your app runs.

## Installation
```bash
git clone https://github.com/yourusername/configguard.git
cd configguard
pip install -e .
```

## Usage
```python
from configguard import Schema, Field, validate
from configguard.errors import ValidationError

schema = Schema({
    'host': Field(type=str, required=True),
    'port': Field(type=int, required=True, min=1, max=65535),
    'username': Field(type=str, required=True)
})

try:
    validate(config, schema)
    print("Config is valid!")
except ValidationError as e:
    print(f"Invalid config: {e}")
```

## Supported File Formats
- YAML
- JSON
- TOML

## Field Options
- `type` — expected type (`str`, `int`, `bool`, etc.)
- `required` — whether the field must be present (default: `False`)
- `min` — minimum value for numbers (optional)
- `max` — maximum value for numbers (optional)

## Running Tests
```bash
pytest
```