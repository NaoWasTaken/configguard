import pytest
from configguard import parsers
from configguard.errors import FileFormatError

def test_load_yaml(tmp_path):
    f = tmp_path / "config.yaml"
    f.write_text("host: localhost\nport: 5432")
    result = parsers.load_yaml(f)
    assert result == {'host': 'localhost', 'port': 5432}

def test_load_json(tmp_path):
    f = tmp_path / "config.json"
    f.write_text('{"host": "localhost", "port": 5432}')
    result = parsers.load_json(f)
    assert result == {'host': 'localhost', 'port': 5432}

def test_load_toml(tmp_path):
    f = tmp_path / "config.toml"
    f.write_text('host = "localhost"\nport = 5432')
    result = parsers.load_toml(f)
    assert result == {'host': 'localhost', 'port': 5432}

def test_invalid_yaml(tmp_path):
    f = tmp_path / "bad.yaml"
    f.write_text("}{invalid yaml}{")
    with pytest.raises(FileFormatError):
        parsers.load_yaml(f)