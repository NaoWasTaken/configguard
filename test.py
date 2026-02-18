from configguard import Schema, Field, validate

schema = Schema({
    'host': Field(type=str, required=True),
    'port': Field(type=int, required=True, min=1, max=65535)
})

config = {'host': 'localhost'}

validate(config, schema)
print("Valid config passed!")