from .errors import ValidationError

def validate(config, schema):
    for key in schema.structure:
        field = schema.structure[key]
        if key in config:
            if not isinstance(config[key], field.type):
                raise ValidationError(f"{key} could not be validated (type error)!")
            if field.min != None and field.max != None:
                if config[key] < field.min or config[key] > field.max:
                    raise ValidationError(f"{key} could not be validated (value out of range)!")
        else:
            if field.required:
                raise ValidationError(f"{key} could not be validated (does not exist)!")