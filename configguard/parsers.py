import yaml
import json
import tomllib
from .errors import FileFormatError

def load_yaml(filepath):
    try:
        with open(filepath) as fd:
            return yaml.safe_load(fd)
    except Exception as e:
        raise FileFormatError(f"Could not parse YAML file: {e}")
    
def load_json(filepath):
    try:
        with open(filepath) as fd:
            return json.load(fd)
    except Exception as e:
        raise FileFormatError(f"Could not parse JSON file: {e}")
    
def load_toml(filepath):
    try:
        with open(filepath, 'rb') as fd:
            return tomllib.load(fd)
    except Exception as e:
        raise FileFormatError(f"Could not parse TOML file: {e}")