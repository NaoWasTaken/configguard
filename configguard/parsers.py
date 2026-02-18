import yaml
import json
import tomllib

def load_yaml(filepath):
    with open(filepath) as fd:
        return yaml.safe_load(fd)
    
def load_json(filepath):
    with open(filepath) as fd:
        return json.load(fd)
    
def load_toml(filepath):
    with open(filepath, 'rb') as fd:
        return tomllib.load(fd)